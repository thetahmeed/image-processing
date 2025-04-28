import numpy as np
import cv2 as cv
import os
import glob

def apply_histogram_equalization(source_path, dest_dir):
    """
    Apply histogram equalization to images and save results
    
    Args:
        source_path (str): Path to source image(s) or directory
        dest_dir (str): Directory to save equalized images
    """
    # Ensure the output directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Get all matching image files
    image_files = []
    if os.path.isdir(source_path):
        # If source_path is a directory, look for images inside it
        for ext in ['.jpeg', '.jpg', '.png', '.bmp', '.tiff']:
            pattern = os.path.join(source_path, f'*{ext}')
            image_files.extend(glob.glob(pattern))
    elif '*' in source_path:
        # If source_path contains wildcards, use it directly
        image_files = glob.glob(source_path)
    else:
        # Single file
        if os.path.isfile(source_path):
            image_files = [source_path]
    
    total_images = len(image_files)
    
    if total_images == 0:
        print(f"No images found matching {source_path}")
        return
    
    print(f"Starting histogram equalization on {total_images} images...")
    processed_count = 0
    
    for i, img_path in enumerate(image_files, 1):
        # Read image
        img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"Error: Could not read image {img_path}")
            continue
        
        # Apply histogram equalization
        equ = cv.equalizeHist(img)
        
        # Create comparison image (original and equalized side by side)
        # res = np.hstack((img, equ))
        
        # Generate output filename - keep original name
        base_name = os.path.basename(img_path)
        output_path = os.path.join(dest_dir, base_name)
        
        # Save image
        cv.imwrite(output_path, equ)
        processed_count += 1
        
        # Print progress
        print(f"Processed {i}/{total_images} images ({i} done, {total_images-i} left) - {(i/total_images)*100:.1f}% complete")
    
    print(f"Histogram equalization completed! {processed_count} images processed successfully.")

def apply_clahe_equalization(source_path, dest_dir, clip_limit=2.0, tile_grid_size=(8, 8)):
    """
    Apply CLAHE equalization to images and save results
    
    Args:
        source_path (str): Path to source image(s) or directory
        dest_dir (str): Directory to save equalized images
        clip_limit (float): Threshold for contrast limiting
        tile_grid_size (tuple): Size of grid for histogram equalization
    """
    # Ensure the output directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Get all matching image files
    image_files = []
    if os.path.isdir(source_path):
        # If source_path is a directory, look for images inside it
        for ext in ['.jpeg', '.jpg', '.png', '.bmp', '.tiff']:
            pattern = os.path.join(source_path, f'*{ext}')
            image_files.extend(glob.glob(pattern))
    elif '*' in source_path:
        # If source_path contains wildcards, use it directly
        image_files = glob.glob(source_path)
    else:
        # Single file
        if os.path.isfile(source_path):
            image_files = [source_path]
    
    total_images = len(image_files)
    
    if total_images == 0:
        print(f"No images found matching {source_path}")
        return
    
    print(f"Starting CLAHE equalization on {total_images} images...")
    processed_count = 0
    
    # Create CLAHE object
    clahe = cv.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    
    for i, img_path in enumerate(image_files, 1):
        # Read image
        img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"Error: Could not read image {img_path}")
            continue
        
        # Apply CLAHE
        cl1 = clahe.apply(img)
        
        # Create comparison image (original and equalized side by side)
        # res = np.hstack((img, cl1))
        
        # Generate output filename - keep original name
        base_name = os.path.basename(img_path)
        output_path = os.path.join(dest_dir, base_name)
        
        # Save image
        cv.imwrite(output_path, cl1)
        processed_count += 1
        
        # Print progress
        print(f"Processed {i}/{total_images} images ({i} done, {total_images-i} left) - {(i/total_images)*100:.1f}% complete")
    
    print(f"CLAHE equalization completed! {processed_count} images processed successfully.")

# Call histogram equalization function as requested
if __name__ == "__main__":
    source_path = '/Users/tahmeed/Developer/Projects/Thesis/image-processing/before-equlization'
    dest_dir = '/Users/tahmeed/Developer/Projects/Thesis/image-processing/after-equalization/histogram'
    apply_histogram_equalization(source_path, dest_dir)
