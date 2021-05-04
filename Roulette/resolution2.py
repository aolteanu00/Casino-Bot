from PIL import Image, ImageFilter

im = Image.open('test3.png')

im1 = im.filter(ImageFilter.SHARPEN)
im2 = im1.filter(ImageFilter.BLUR)
im3 = im2.filter(ImageFilter.SMOOTH_MORE)
im3.save("test4.png", dpi=(70,70)) # same as MinFilter(3)
im3.show()
