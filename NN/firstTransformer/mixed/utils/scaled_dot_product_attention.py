import math
import torch
from torch import nn
import torch.nn.functional as F
# Example when d_model = 512 and num_heads = 8
def scaled_dot_product(q, k, v, mask=None):
    d_k = q.size()[-1] # 64
    scaled = torch.matmul(q, k.transpose(-1, -2)) / math.sqrt(d_k) # 30 x 8 x 200 x 200
    if mask is not None:
        scaled = scaled.permute(1, 0, 2, 3) + mask
        scaled = scaled.permute(1, 0, 2, 3) # 30 x 8 x 200 x 200
    attention = F.softmax(scaled, dim=-1) # 30 x 8 x 200 x 200 in a probability distribution
    values = torch.matmul(attention, v) # 30 x 8 x 200 x 64
    return values, attention