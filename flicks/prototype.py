from subprocess import call
import os
import pyautogui
from PIL import Image, ImageChops
import tempfile



def set_image_dpi_resize(image):
    """
    Rescaling image to 300dpi while resizing
    :param image: An image
    :return: A rescaled image
    """
    length_x, width_y = image.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    image_resize = image.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='1.png')
    temp_filename = temp_file.name
    image_resize.save(temp_filename, dpi=(300, 300))
    return temp_filename





print("*")
print("*")
print("*")
print("DRIPBOT IS LIVE")
print("_________________________________________________________________________")

#CAPTURES SCREENGRAB, SAVES TO SAME DIRECTORY
call(["screencapture", "-R305,235,90,30", "test.png"])

#PILLOW IMAGE MANIPULATION
image = Image.open('test.png')
image.show()
image.show('test.png')
image2 = image.resize((1920,1080))
image2.show()
inv_image = ImageChops.invert(image)
inv_image.show()

image3 = set_image_dpi_resize(image)
print(image3)

image.save('test1.png')
image2.save('test2.png')
inv_image.save('test3.png')

image2.show()
inv_image.show()

#OCR ANALYZES SCREENGRAB AND PROVIDES A .TXT FILE INTERPRETATION IN THE SAME DIRECTORY
os.system('tesseract test1.png tess.txt')
os.system('tesseract test2.png tess.txt')
os.system('tesseract test3.png tess.txt')






#CONVERTS IMAGE TO GRAYSCALEs
def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

#if __name__ == '__main__':
#    black_and_white('screenshot2.jpg','bw3_screenshot.jpg')

#EXAMPLE LOOP
#re-bet coordinates: (1167,420)
#re-betx2 coordinates: (1154,544)
#pyautogui example syntax: pyautogui.click(x=1154, y=5444, clicks=1, interval=20, button='left')
#x = 0
#while x < 10:
#    pyautogui.click(x=1154, y=544, clicks=1, button='left')
#    pyautogui.click(x=1154, y=544, clicks=1, button='left')
#    pyautogui.click(interval = 7)
#    x+=1

print("_________________________________________________________________________")
print("DRIPBOT OUT")
print("*")
print("*")
print("*")
