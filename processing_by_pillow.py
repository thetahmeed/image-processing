from PIL import Image
image = Image.open("images/color_image1.png")

# RGB to HSV in Pillow
image = image.convert('RGB')
hsv = image.convert('HSV')
image.save('output/pillow/hsv_image.jpg')

# Resizing
resized = image.resize((224, 224))
resized.save('output/pillow/resized_image_244x244.jpg')

# Cropping
width, height = image.size
size = min (width, height)
left = (width - size) / 2
top = (height - size) / 2
right = (width + size) / 2
bottom = (height + size) / 2
cropped = image.crop((left, top, right, bottom))
cropped.save('output/pillow/cropped_image.jpg')
