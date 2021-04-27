from PIL import Image, ImageFilter

im1 = Image.open(r"/Users/dominicesposito/Desktop/Bot/flicks/screenshot.jpg")
im2 = im1.filter(ImageFilter.BoxBlur(5))
im2.show()
