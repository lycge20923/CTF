
from PIL import Image


image = Image.open('Image_Magic/out copy.jpg')
image = image.convert('RGB')
pixels = image.load()
length, _ = image.size


image_fix = Image.new(image.mode, (304, length//304))
pixels_fix = image_fix.load()

for x in range(length):
    pixels_fix[x // (length//304), x % (length//304)] = pixels[x, 0]

image_fix.save('Image_Magic/out copy-fix.jpg')
