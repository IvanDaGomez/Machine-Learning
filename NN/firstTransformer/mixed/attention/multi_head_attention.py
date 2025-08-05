from torch import nn
from mixed.utils.scaled_dot_product_attention import scaled_dot_product

# Example when d_model = 512 and num_heads = 8
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model # 512
        self.num_heads = num_heads # 8
        self.head_dim = d_model // num_heads # 64
        self.qkv_layer = nn.Linear(d_model , 3 * d_model) # 512 -> 1536
        self.linear_layer = nn.Linear(d_model, d_model) # 512 -> 512
    
    def forward(self, x, mask):
        batch_size, sequence_length, d_model = x.size() # 30 x 200 x 512
        qkv = self.qkv_layer(x) # 30 x 200 x 1536
        qkv = qkv.reshape(batch_size, sequence_length, self.num_heads, 3 * self.head_dim) # 30 x 200 x 8 x 192
        qkv = qkv.permute(0, 2, 1, 3) # 30 x 8 x 200 x 192
        q, k, v = qkv.chunk(3, dim=-1) # q,k, v = 30 x 8 x 200 x 64
        values, attention = scaled_dot_product(q, k, v, mask) # 30 x 8 x 200 x 64, 30 x 8 x 200 x 200
        values = values.permute(0, 2, 1, 3) # 30 x 200 x 8 x 64
        values = values.reshape(batch_size, sequence_length, self.num_heads * self.head_dim) # 30 x 200 x 512
        out = self.linear_layer(values) # 30 x 200 x 512
        return out
