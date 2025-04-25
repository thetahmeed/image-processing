import cv2
image = cv2.imread("images/color_image.png")

# BGR to Grayscale in OpenCV
gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

# Resizing and Cropping
resized = cv2.resize(image, (224, 224))

# To crop an image to a square
height, width = image.shape[:2]
size = min(width, height)
x = (width - size) // 2
y = (height - size) // 2
cropped = image[y:y+size, x:x+size]

cv2.imwrite('output/cropped_image.png', cropped)


