import numpy as np
import cv2
image = cv2.imread("images/color_image1.png")

# # BGR to Grayscale in OpenCV
# gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('output/cv2/gray_image.png', gray)

# # Resizing and Cropping
# resized = cv2.resize(image, (224, 224))
# cv2.imwrite('output/cv2/resized_image_244x244.png', resized)

# # To crop an image to a square
# height, width = image.shape[:2]
# size = min(width, height)
# x = (width - size) // 2
# y = (height - size) // 2
# cropped = image[y:y+size, x:x+size]

# cv2.imwrite('output/cv2/cropped_image.png', cropped)

# # Negetive image
# negative = cv2.bitwise_not(image)
# cv2.imwrite('output/cv2/negative_image.png', negative)

# # Thresholding
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imwrite('output/cv2/threshold_image.png', thresh)

# # Logarithmic Transformation
# c = 255 / (np.log(1 + np.max(image)))
# log_transformed = c * (np.log(1 + image))
# log_transformed = np.array(log_transformed, dtype=np.uint8)
# cv2.imwrite('output/cv2/log_transformed_image.png', log_transformed)

# Power-Law Transformation
# gamma = 2.0
# c = 255 / (np.max(image) ** gamma)
# power_law_transformed = c * (image ** gamma)
# power_law_transformed = np.array(power_law_transformed, dtype=np.uint8)
# cv2.imwrite('output/cv2/power_law_transformed_image.png', power_law_transformed)

# # Piecewise Linear Transformation
# def piecewise_linear_transformation(image, r1, s1, r2, s2):
#     # Create a copy of the image
#     transformed_image = np.zeros_like(image)
#     # Apply the piecewise linear transformation
#     transformed_image[image < r1] = (s1 / r1) * image[image < r1]
#     transformed_image[(image >= r1) & (image <= r2)] = s1 + ((s2 - s1) / (r2 - r1)) * (image[(image >= r1) & (image <= r2)] - r1)
#     transformed_image[image > r2] = s2 + ((255 - s2) / (255 - r2)) * (image[image > r2] - r2)
#     return transformed_image
# r1 = 100
# s1 = 50
# r2 = 200
# s2 = 150
# piecewise_transformed = piecewise_linear_transformation(image, r1, s1, r2, s2)
# cv2.imwrite('output/cv2/piecewise_transformed_image.png', piecewise_transformed)
