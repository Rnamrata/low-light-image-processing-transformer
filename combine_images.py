
from PIL import Image
import os

# List of input image paths
input_images = [
    "visualization/LOLv1/compared_image_22_8.png",
    "visualization/LOLv1/compared_image_493_8.png",
    "visualization/LOLv1/compared_image_547_8.png",
    "visualization/LOLv1/compared_image_665_8.png",
    "visualization/LOLv1/compared_image_778_8.png"
]

# Output path
output_path = "visualization/LOLv1"

# Load images
images = [Image.open(img) for img in input_images]

# Get dimensions of the first image
width, height = images[0].size

# Create a new image with enough space to hold all images in a column
merged_image = Image.new('RGB', (width, height * len(images)))

# Paste images into the merged image
for i, img in enumerate(images):
    merged_image.paste(img, (0, i * height))

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Save the merged image
output_image_path = os.path.join(output_path, "combined_compare_image_vertical_8.png")
merged_image.save(output_image_path)

print(f"Merged image saved at: {output_image_path}")
