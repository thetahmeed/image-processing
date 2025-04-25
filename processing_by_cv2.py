import cv2
image = cv2.imread("images/color_image1.png")

# BGR to Grayscale in OpenCV
gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output/cv2/gray_image.png', gray)

# Resizing and Cropping
resized = cv2.resize(image, (224, 224))
cv2.imwrite('output/cv2/resized_image_244x244.png', resized)

# To crop an image to a square
height, width = image.shape[:2]
size = min(width, height)
x = (width - size) // 2
y = (height - size) // 2
cropped = image[y:y+size, x:x+size]

cv2.imwrite('output/cv2/cropped_image.png', cropped)


