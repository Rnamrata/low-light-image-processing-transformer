from PIL import Image
import os

# List of input image paths
input_images = [
    "datasets/LOLdataset/eval15/low/547.png",
    "datasets/LOLdataset/eval15/high/547.png",
    "results/LOLv1/epoch_420/547.png",
    "output/LOLv1//547.png",
]

# Output path
output_path = "visualization/LOLv1"

# Load images
images = [Image.open(img) for img in input_images]

# Get dimensions of the first image
width, height = images[0].size

# Create a new image with enough space to hold all images in a row
merged_image = Image.new('RGB', (width * len(images), height))

# Paste images into the merged image
for i, img in enumerate(images):
    merged_image.paste(img, (i * width, 0))

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Save the merged image
output_image_path = os.path.join(output_path, "compared_image_547_8.png")
merged_image.save(output_image_path)

print(f"Merged image saved at: {output_image_path}")
