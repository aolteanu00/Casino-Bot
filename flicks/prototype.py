from subprocess import call
import os
import pyautogui
from PIL import Image, ImageChops
import PIL.ImageOps

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

image2 = image.resize((1920,1080))
image2.show()

#inv_image = ImageChops.invert(image)
#inv_image.show()

image.save('test1.png')
image2.save('test2.png')
#inv_image.save('test3.png')

if image.mode == 'RGBA':
    r,g,b,a = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))

    inverted_image = PIL.ImageOps.invert(rgb_image)

    r2,g2,b2 = inverted_image.split()

    final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

    final_transparent_image.save('test4.png')

else:
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('test4.png')

image4 = Image.open('test4.png')
image4.show()

#OCR ANALYZES SCREENGRAB AND PROVIDES A .TXT FILE INTERPRETATION IN THE SAME DIRECTORY
os.system('tesseract test1.png test1')
os.system('tesseract test2.png test2')
#os.system('tesseract test3.png tess.txt')
os.system('tesseract test4.png test4')


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
