import torch
from torch import nn
from mixed.utils.scaled_dot_product_attention import scaled_dot_product
# Example when d_model = 512 and num_heads = 8
class MultiHeadCrossAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model # 512
        self.num_heads = num_heads # 8
        self.head_dim = d_model // num_heads # 64
        self.kv_layer = nn.Linear(d_model , 2 * d_model) # 512 -> 1024
        self.q_layer = nn.Linear(d_model , d_model) # 512 -> 512
        self.linear_layer = nn.Linear(d_model, d_model) # 512 -> 512
    
    def forward(self, x, y, mask):
        batch_size, sequence_length, d_model = x.size() # in practice, this is the same for both languages...so we can technically combine with normal attention
        kv = self.kv_layer(x) # 30 x 200 x 1024
        q = self.q_layer(y) # 30 x 8 x 200 x 512
        kv = kv.reshape(batch_size, sequence_length, self.num_heads, 2 * self.head_dim) # 30 x 200 x 8 x 128
        q = q.reshape(batch_size, sequence_length, self.num_heads, self.head_dim) # 30 x 200 x 8 x 64
        kv = kv.permute(0, 2, 1, 3) # 30 x 8 x 200 x 128
        q = q.permute(0, 2, 1, 3) # 30 x 8 x 200 x 64
        k, v = kv.chunk(2, dim=-1) # k, v = 30 x 8 x 200 x 64
        # dot product attentopn requires q, k, v to be of shape (batch_size, num_heads, sequence_length, head_dim)
        values, attention = scaled_dot_product(q, k, v, mask) # We don't need the mask for cross attention, removing in outer function!
        values = values.permute(0, 2, 1, 3) # 30 x 200 x 8 x 64
        values = values.reshape(batch_size, sequence_length, d_model) # 30 x 200 x 512
        out = self.linear_layer(values) # 30 x 200 x 512
        return out
