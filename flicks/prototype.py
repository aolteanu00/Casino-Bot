from subprocess import call
import os
import pyautogui
from PIL import Image, ImageChops

print("*")
print("*")
print("*")
print("DRIPBOT IS LIVE")
print("_________________________________________________________________________")

#CAPTURES SCREENGRAB, SAVES TO SAME DIRECTORY
call(["screencapture", "-R305,235,90,30", "test.pdf"])

#PILLOW IMAGE MANIPULATION
image = Image.open('test.pdf')
image.show()
image.show('test.pdf')
image2 = image.resize((1920,1080))
image2.show()
inv_image = ImageChops.invert(image)
inv_image.show()

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
