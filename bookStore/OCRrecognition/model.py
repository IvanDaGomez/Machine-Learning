import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten").to(device)
visionEncoderModel = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten").to(device)

class OCR_TO_CLASSES_MODEL(nn.Module):
    def __init__(self, d_model, 
                          ffn_hidden,
                          num_heads, 
                          drop_prob, 
                          num_layers, 
                          max_sequence_length,
                          sp_vocab_size):
        super().__init__()
        self.processor = processor
        self.visionEncoderModel = visionEncoderModel
        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=num_heads,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=ffn_hidden,
            dropout=drop_prob,
            activation='relu',
            norm_first=True,
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu"),
            batch_first=True,
            max_seq_length=max_sequence_length

        )
        
    def forward(self, x):


    def predict(self, x):

    def plot(self, x, y):

    def confusion_matrix(self, y_true, y_pred):
    
