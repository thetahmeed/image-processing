import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from tqdm import tqdm  # For progress bar

# Check image path and load the noisy image
image_path = "images/noisy_image_2.png"
print(f"Looking for image at: {os.path.abspath(image_path)}")

if not os.path.exists(image_path):
    print(f"Error: Image file not found at {image_path}")
    print("Current working directory:", os.getcwd())
    print("Available files in images/ directory (if it exists):")
    if os.path.exists("images"):
        print(os.listdir("images"))
    else:
        print("images/ directory doesn't exist")
    exit()

# Load image and resize to make processing faster
noisy_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if noisy_image is None:
    print(f"Error: Failed to load image {image_path}")
    exit()

print(f"Original image shape: {noisy_image.shape}")

# Resize image for faster processing (optional)
resize_factor = 0.25  # Resize to 25% of original size
resized_image = cv2.resize(noisy_image, None, fx=resize_factor, fy=resize_factor, 
                           interpolation=cv2.INTER_AREA)
print(f"Resized image shape: {resized_image.shape}")

# Convert to float32 for processing
processed_image = resized_image.astype(np.float32)

# IQR-Based Denoising Function with progress bar
def iqr_denoise(image, window_size=3, threshold_scale=1.5):
    padded_image = np.pad(image, pad_width=window_size // 2, mode='reflect')
    denoised = np.copy(image)
    
    print("Starting denoising process...")
    height, width = image.shape
    total_pixels = height * width
    
    # Process in row batches to show progress
    with tqdm(total=height, desc="Denoising") as pbar:
        for i in range(height):
            for j in range(width):
                window = padded_image[i:i + window_size, j:j + window_size].flatten()
                q1 = np.percentile(window, 25)
                q3 = np.percentile(window, 75)
                iqr = q3 - q1
                lower = q1 - threshold_scale * iqr
                upper = q3 + threshold_scale * iqr
                center_pixel = padded_image[i + window_size // 2, j + window_size // 2]

                if center_pixel < lower or center_pixel > upper:
                    denoised[i, j] = np.median(window)
            pbar.update(1)
    
    print("Denoising completed")
    return denoised

# Apply IQR denoising
print("Applying IQR denoising...")
start_time = time.time()
iqr_denoised_image = iqr_denoise(processed_image)
end_time = time.time()
print(f"Denoising completed in {end_time - start_time:.2f} seconds")

# Display results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(processed_image, cmap='gray')
plt.title("Noisy Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(iqr_denoised_image, cmap='gray')
plt.title("IQR Denoised Image")
plt.axis('off')

plt.tight_layout()
print("Displaying images...")
plt.show()

# Save the denoised image
output_path = "output/denoised_image_using_iqr.png"
cv2.imwrite(output_path, iqr_denoised_image)
print(f"Denoised image saved at: {output_path}")

