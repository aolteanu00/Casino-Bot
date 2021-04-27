from subprocess import call
import os
import pyautogui
from PIL import Image, ImageOps

print("*")
print("*")
print("*")
print("DRIPBOT IS LIVE")
print("_________________________________________________________________________")
call(["screencapture", "-R390,280,150,50", "test.jpg"])


image = Image.open('test.jpg')
new_image = image.resize((250, 50))
new_image.save("test.png")


#CAPTURES A SCREEN GRAB OF CURRENT BALANCE
# Captures area of screen
#CONVERTS IMAGE TO GRAYSCALE
def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

def image_inversion(inv_image, output_path):
    img = Image.open(inv_image)
    img = PIL.ImageChops.invert(inv_image)
    img.save(output_path)
#OCR ANALYZES SCREENGRAB AND PROVIDES A .TXT FILE INTERPRETATION IN THE SAME DIRECTORY


#if __name__ == '__main__':
if __name__ == '__main__':
    black_and_white("test.png", "test1.png")
    image_inversion("test1.png", "test2.png")

os.system('tesseract test2.png --psm 6')


#    black_and_white('screenshot2.jpg','bw3_screenshot.jpg'

#re-bet coordinates: (1167,420)
#re-betx2 coordinates: (1154,544)
#pyautogui example syntax: pyautogui.click(x=1154, y=5444, clicks=1, interval=20, button='left')

#EXAMPLE FOR LOOP
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
