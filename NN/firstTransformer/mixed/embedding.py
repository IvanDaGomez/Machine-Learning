import torch
from torch import nn
from mixed.positional_encoding import PositionalEncoding
from mixed.utils.get_device import get_device
class SentenceEmbedding(nn.Module):
    "For a given sentence, create an embedding"
    def __init__(self, max_sequence_length, d_model, language_to_index, START_TOKEN, END_TOKEN, PADDING_TOKEN):
        super().__init__()
        self.vocab_size = len(language_to_index) # Number of unique words (or tokens) in the language
        self.max_sequence_length = max_sequence_length # Maximum length of a sentence
        self.embedding = nn.Embedding(self.vocab_size, d_model) # Embedding using already trained word embeddings
        self.language_to_index = language_to_index # Dictionary mapping words to unique indices
        self.position_encoder = PositionalEncoding(d_model, max_sequence_length) # Positional Encoding
        self.dropout = nn.Dropout(p=0.1)
        self.START_TOKEN = START_TOKEN
        self.END_TOKEN = END_TOKEN
        self.PADDING_TOKEN = PADDING_TOKEN
    
    def batch_tokenize(self, batch, start_token, end_token):

        def tokenize(sentence, start_token, end_token):
            sentence_word_indicies = [self.language_to_index[token] for token in list(sentence)]
            if start_token:
                sentence_word_indicies.insert(0, self.language_to_index[self.START_TOKEN])
            if end_token:
                sentence_word_indicies.append(self.language_to_index[self.END_TOKEN])
            for _ in range(len(sentence_word_indicies), self.max_sequence_length):
                sentence_word_indicies.append(self.language_to_index[self.PADDING_TOKEN])
            return torch.tensor(sentence_word_indicies) # returns a tensor with all words converted into the dictionary index with padding and tokens

        tokenized = []
        for sentence_num in range(len(batch)): # for each batch of sentences tokenizr
           tokenized.append( tokenize(batch[sentence_num], start_token, end_token) )
        tokenized = torch.stack(tokenized) 
        return tokenized.to(get_device()) # send the tensor to the device
    
    def forward(self, x, start_token, end_token): # sentence
        x = self.batch_tokenize(x, start_token, end_token) # tokenize all batches
        x = self.embedding(x) # create the vector
        pos = self.position_encoder().to(get_device()) # positional encoding to the device
        x = self.dropout(x + pos)
        return x