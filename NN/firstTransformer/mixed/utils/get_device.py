import torch
# Optimizations using cuda
def get_device():
    return torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
