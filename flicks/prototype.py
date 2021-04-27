from subprocess import call
import os
import pyautogui
from PIL import Image

print("*")
print("*")
print("*")
print("DRIPBOT IS LIVE")
print("_________________________________________________________________________")
call(["screencapture", "-R305,235,90,30", "screenshot7.jpg"])


image = Image.open('screenshot7.jpg')
new_image = image.resize((1024, 1024))
image.show()

image.save('screenshot8.png')

#CAPTURES A SCREEN GRAB OF CURRENT BALANCE
# Captures area of screen

#OCR ANALYZES SCREENGRAB AND PROVIDES A .TXT FILE INTERPRETATION IN THE SAME DIRECTORY
os.system('tesseract screenshot7.jpg --psm 6')

#CONVERTS IMAGE TO GRAYSCALE
def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

#if __name__ == '__main__':
#    black_and_white('screenshot2.jpg','bw3_screenshot.jpg')

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
