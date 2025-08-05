from torch import nn
from mixed.embedding import SentenceEmbedding
from mixed.layer_normalization import LayerNormalization
from mixed.attention.multi_head_attention import MultiHeadAttention
from mixed.attention.multi_head_cross_attention import MultiHeadCrossAttention
from mixed.feed_forward import PositionwiseFeedForward

class Decoder(nn.Module):
    def __init__(self, 
                 d_model, 
                 ffn_hidden, 
                 num_heads, 
                 drop_prob, 
                 num_layers,
                 max_sequence_length,
                 language_to_index,
                 START_TOKEN,
                 END_TOKEN, 
                 PADDING_TOKEN):
        super().__init__()
        self.sentence_embedding = SentenceEmbedding(max_sequence_length, d_model, language_to_index, START_TOKEN, END_TOKEN, PADDING_TOKEN)
        self.layers = SequentialDecoder(*[DecoderLayer(d_model, ffn_hidden, num_heads, drop_prob) for _ in range(num_layers)])

    def forward(self, x, y, self_attention_mask, cross_attention_mask, start_token, end_token):
        y = self.sentence_embedding(y, start_token, end_token) # Encoding 
        y = self.layers(x, y, self_attention_mask, cross_attention_mask) # Steps in the transformer decoder
        return y
    

class DecoderLayer(nn.Module):
    def __init__(self, d_model, ffn_hidden, num_heads, drop_prob):
        super(DecoderLayer, self).__init__()
        self.self_attention = MultiHeadAttention(d_model=d_model, num_heads=num_heads) # masked multi-head attention
        self.layer_norm1 = LayerNormalization(parameters_shape=[d_model]) # layer normalization
        self.dropout1 = nn.Dropout(p=drop_prob) # dropout

        self.encoder_decoder_attention = MultiHeadCrossAttention(d_model=d_model, num_heads=num_heads)
        self.layer_norm2 = LayerNormalization(parameters_shape=[d_model])
        self.dropout2 = nn.Dropout(p=drop_prob)

        self.ffn = PositionwiseFeedForward(d_model=d_model, hidden=ffn_hidden, drop_prob=drop_prob)
        self.layer_norm3 = LayerNormalization(parameters_shape=[d_model])
        self.dropout3 = nn.Dropout(p=drop_prob)

    def forward(self, x, y, self_attention_mask, cross_attention_mask):
        _y = y.clone() # residual connection
        y = self.self_attention(y, mask=self_attention_mask) # masked multi-head attention
        y = self.dropout1(y) # dropout
        y = self.layer_norm1(y + _y) # add with residual conection # 30 x 200 x 512

        _y = y.clone()
        y = self.encoder_decoder_attention(x, y, mask=cross_attention_mask) # cross attention
        y = self.dropout2(y)
        y = self.layer_norm2(y + _y)

        _y = y.clone()
        y = self.ffn(y) # feed forward 512 -> 2048 -> 512
        y = self.dropout3(y)
        y = self.layer_norm3(y + _y)
        return y

class SequentialDecoder(nn.Sequential):
    def forward(self, *inputs): # we do this to repeat the decoder process
        x, y, self_attention_mask, cross_attention_mask = inputs
        for module in self._modules.values():
            y = module(x, y, self_attention_mask, cross_attention_mask)
        return y
