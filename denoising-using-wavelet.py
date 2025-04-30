import numpy as np
import pywt
import matplotlib.pyplot as plt
import cv2

# Load a grayscale image and add random noise
image = cv2.imread(cv2.samples.findFile("images/COVID19(153).jpg"), cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (256, 256))  # Resize for faster processing

# Add Gaussian noise
# np.random.seed(0)
# noisy_image = image + 20 * np.random.randn(*image.shape)
# noisy_image = np.clip(noisy_image, 0, 255)

# Perform wavelet transform
wavelet = 'coif1' # 'db8', 'sym4', or 'coif1' 
# coeffs = pywt.wavedec2(noisy_image, wavelet, level=2)
coeffs = pywt.wavedec2(image, wavelet, level=2)

# Thresholding - soft thresholding
# threshold = 10
threshold = np.median(np.abs(coeffs[1][0])) / 0.6745  # universal threshold
coeffs_thresh = list(coeffs)
coeffs_thresh[1:] = [(pywt.threshold(cH, threshold, mode='soft'),
                      pywt.threshold(cV, threshold, mode='soft'),
                      pywt.threshold(cD, threshold, mode='soft'))
                     for cH, cV, cD in coeffs[1:]]

# Reconstruct the image
denoised_image = pywt.waverec2(coeffs_thresh, wavelet)
denoised_image = np.clip(denoised_image, 0, 255)

# Plot the original, noisy, and denoised images
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(noisy_image, cmap='gray')
# plt.title("Noisy Image")
# plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title("Wavelet Denoised Image")
plt.axis('off')

plt.tight_layout()
plt.show()
