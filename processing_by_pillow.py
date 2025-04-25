from PIL import Image
image = Image.open("images/color_image.png")

# RGB to HSV in Pillow
image = image.convert('HSV')

# Resizing
resized = image.resize((224, 224))

# Cropping
width, height = image.size
size = min (width, height)
left = (width - size) / 2
top = (height - size) / 2
right = (width + size) / 2
bottom = (height + size) / 2
cropped = image.crop((left, top, right, bottom))
