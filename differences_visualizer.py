import matplotlib.pyplot as plt
import numpy as np
import cv2  

def plot_pixel_intensity_profile(noisy_img, denoised_img, original_img=None, row=128):

    plt.figure(figsize=(10, 4))
    plt.plot(noisy_img[row], label='Noisy', color='red', linestyle='--')
    plt.plot(denoised_img[row], label='Denoised', color='blue')
    
    if original_img is not None:
        plt.plot(original_img[row], label='Original', color='green', alpha=0.5)
    
    plt.title(f'Pixel Intensity')
    plt.xlabel('Pixel Position')
    plt.ylabel('Intensity')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_histogram_comparison(noisy_img, denoised_img, original_img=None):

    plt.figure(figsize=(10, 4))
    plt.hist(noisy_img.ravel(), bins=150, alpha=0.5, label='Noisy', color='red')
    plt.hist(denoised_img.ravel(), bins=150, alpha=0.5, label='Denoised', color='blue')
    
    if original_img is not None:
        plt.hist(original_img.ravel(), bins=150, alpha=0.3, label='Original', color='green')
    
    plt.title("Histogram of Pixel Intensities")
    plt.xlabel("Intensity Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()


noisy_path = 'images/noisy_image_2.png' 
denoised_path = 'output/denoised_image_using_wavelet.png'  

noisy_img = cv2.imread(noisy_path, cv2.IMREAD_GRAYSCALE)
denoised_img = cv2.imread(denoised_path, cv2.IMREAD_GRAYSCALE)

if noisy_img is None or denoised_img is None:
    print(f"Error: Could not load images from provided paths.")
else:
    plot_pixel_intensity_profile(noisy_img, denoised_img)
    plot_histogram_comparison(noisy_img, denoised_img)
