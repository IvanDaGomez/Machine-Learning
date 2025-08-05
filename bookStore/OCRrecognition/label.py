# Create a program to open an image and label it manually
from pathlib import Path
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

line_count = 0
path = Path("bookStore/OCRrecognition/data/")
image_path = path / "images"
image_path.mkdir(parents=True, exist_ok=True)
label_path = path / "labels"
label_path.mkdir(parents=True, exist_ok=True)
# Check if labels.txt exists, if not create it
line_count = 0
try:
    with open(label_path/ 'labels.txt', "r") as f:
        lines = f.readlines()
        line_count = len(lines)
except FileNotFoundError:
    line_count = 0
print(f"Number of lines in labels.txt: {line_count}")
# Create a program to open an image and label it manually
image_list = [x for x in os.listdir(image_path) if x.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_list = image_list[line_count:]
print(f"Number of images to label: {len(image_list)}")


for i, image_name in enumerate(image_list):
    img_full_path = os.path.join(image_path, image_name)

    # Load and display image using OpenCV
    image = cv2.imread(img_full_path)
    if image is None:
        print(f"⚠️ Skipping {image_name} (could not load image)")
        continue

    cv2.imshow("Label this image (press ENTER after typing in terminal)", image)
    cv2.waitKey(500)  # Give the window time to render
    title = input(f"Enter title for image '{image_name}': ")
    title = title.title()
    if (title.lower() == 'q'):
        print("Skipping...")
        continue
    author = input(f"[{i+1}/{len(image_list)}] Enter author for image '{image_name}': ")

    author = author.title()
    
    template = r'<source>{image_name}</source><author>{author}</title>{title}</title>'
    label = template.format(image_name=image_name, author=author, title=title)
    # Save the label to a file
    with open(label_path / 'labels.txt', "a") as f:
        f.write(f"{label}\n")

    print(f"✅ Label saved: '{label}' for image {image_name}")
    cv2.destroyAllWindows()
