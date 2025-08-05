 
from pathlib import Path
import torchvision
from torchvision import transforms
import os
from torch.utils.data import DataLoader
size = 64
   # **Load Dataset**
class ClampTransform:
    def __call__(self, x):
        return x.clamp(0, 1)
    
data_transform = transforms.Compose([
    transforms.Resize(size = (size, size)),
    # Turn the image into a torch.Tensor
    transforms.ToTensor(),
    ClampTransform()
])
def load_data():
    data_path = Path('generativeAI/data')
    celeba_path = data_path / 'celeba'
    celeba_path.mkdir(parents=True, exist_ok=True)
    train_data = torchvision.datasets.CelebA(
        root=celeba_path, 
        split='train',
        download=True,
        transform= data_transform
    )

    test_data = torchvision.datasets.CelebA(
        root=celeba_path, 
        split='test',
        download=True,
        transform= data_transform
    )
    sample_x, sample_y = next(iter(train_data))
    BATCH_SIZE = 128
    NUM_WORKERS = os.cpu_count()
    train_dataloader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)
    test_dataloader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS)
    
    return train_dataloader, test_dataloader
