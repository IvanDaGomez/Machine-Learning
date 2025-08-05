import torch
import transformers
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from pathlib import Path
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from customDataset import ImageOnlyDataset
#from datasets import Dataset
import os
# mps = Metal Performance Shaders for GPU acceleration on macOS
device = torch.device("mps" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
DATA_PATH = Path("bookStore/OCRrecognition/data/images/")
print(torch.backends.mps.is_available())
print(torch.backends.mps.is_built())
def get_train_test_paths(data_path: Path):
    """
    Get the paths to the train and test directories.
    
    Args:
        data_path (Path): The base path to the data.
        
    Returns:
        tuple: Paths to the train and test directories.
    """
    data = os.listdir(data_path)
    percentage = 0.8
    train_size = int(len(data) * percentage)
    train_path, test_path = data[:train_size], data[train_size:]
    return train_path, test_path
train_path, test_path = get_train_test_paths(DATA_PATH)

BATCH_SIZE = 32
os_count = os.cpu_count()
# Load the image
size = 64
custom_transform = transforms.Compose([
    transforms.Resize((size * 3, size * 2)), # Book aspect ratio
    transforms.ToTensor()
])
from torch.utils.data import DataLoader
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch

# Cargar TrOCR
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten").to("mps" if torch.backends.mps.is_available() else "cpu")

dataset = ImageOnlyDataset(image_dir=DATA_PATH, transform=custom_transform)
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

for image, filename in dataloader:
    # Procesar imagen para OCR
    pixel_values = processor(images=image[0], return_tensors="pt").pixel_values.to(device)
    generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    print(f"\n🖼 Imagen: {filename[0]}")
    print(f"📝 OCR: {text}")
# train_data = datasets.ImageFolder(root=TRAIN_PATH,
#                                   transform=custom_transform,
#                                   target_transform=None)
# test_data = datasets.ImageFolder(root=TEST_PATH,
#                                  transform=custom_transform)


# train_dataloader = DataLoader(train_data, 
#                               batch_size=BATCH_SIZE, 
#                               num_workers=os_count,
#                               shuffle=True,
#                               )
# test_dataloader = DataLoader(test_data, 
#                              batch_size=BATCH_SIZE, 
#                              num_workers=os_count,
#                              shuffle=False)
# print(f"Dataloader: {train_dataloader}\nLength: {len(train_dataloader)}\nType: {type(train_dataloader)}")
# print(f'Length of train_dataloader: {len(train_dataloader)} batches of {BATCH_SIZE}')
# print(f'Length of test_dataloader: {len(test_dataloader)} batches of {BATCH_SIZE}')
# ocr_processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten").to(device)
# ocr_model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten").to(device)

# for param in model.parameters():
#     param.requires_grad = False
# print(next(iter(train_dataloader))[0].shape)
# image = next(iter(train_dataloader))[0][0][0]
# def extract_text_from_image(image:Image.Image) -> str:
#     """
#     Extract text from an image using OCR.
    
#     Args:
#         image (Image.Image): The input image.
        
#     Returns:
#         str: The extracted text.
#     """
#     # Preprocess the image
#     pixel_values = ocr_processor(images=image, return_tensors="pt").pixel_values
#     pixel_values = pixel_values.to(device)
    
#     # Generate text using the model
#     generated_ids = ocr_model.generate(pixel_values)
    
#     # Decode the generated IDs to text
#     text = ocr_processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
#     return text


# pixel_values = processor(images=image, return_tensors="pt").pixel_values
# generated_ids = model.generate(pixel_values)
# text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]