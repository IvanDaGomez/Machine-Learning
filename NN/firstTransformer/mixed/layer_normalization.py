import torch
from torch import nn
class LayerNormalization(nn.Module):
    def __init__(self, parameters_shape, eps=1e-5):
        super().__init__()
        self.parameters_shape=parameters_shape
        self.eps=eps
        self.gamma = nn.Parameter(torch.ones(parameters_shape))
        self.beta =  nn.Parameter(torch.zeros(parameters_shape))

    def forward(self, inputs):
        dims = [-(i + 1) for i in range(len(self.parameters_shape))] # get the dimensions of the input
        mean = inputs.mean(dim=dims, keepdim=True) # mean maintining dimensions 30 x 200 x 1
        var = ((inputs - mean) ** 2).mean(dim=dims, keepdim=True) # variance
        std = (var + self.eps).sqrt() # standard deviation
        y = (inputs - mean) / std # normalization 30 x 200 x 512
        out = self.gamma * y + self.beta # trainable parameters
        return out