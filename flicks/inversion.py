
from PIL import Image
import PIL.ImageOps

image = Image.open('test1.png')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('test2.png')
