from subprocess import call
import os
import pyautogui
from PIL import Image
import PIL.ImageOps

print("*")
print("*")
print("*")
print("DRIPBOT IS LIVE")
print("_________________________________________________________________________")
call(["screencapture", "-R390,280,150,50", "test.jpg"])

balance_list = []
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

def invert_colors(image):
    image = Image.open('test1.png')
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('test2.png')

def resize_image():
    basewidth = 500
    img = Image.open('test2.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('test3.png')

def adjust_resolution():
    image_path = "test3.png"
    image_file = Image.open(image_path)
    image_file.save("test4.png", dpi=(500,500))

def tess_run():
    os.system("tesseract test4.png --psm 6")
    file_in = open('--psm.txt', 'r')
    y = file_in.read().split(',')
    w = ''.join(y)
    r = w.replace('\n\x0c', '')
    q = float(r)
    z = balance_list.append(q)
    print(balance_list)


#OCR ANALYZES SCREENGRAB AND PROVIDES A .TXT FILE INTERPRETATION IN THE SAME DIRECTORY

#if __name__ == '__main__':
i = 0
while i < 4:

    if __name__ == '__main__':
        x = black_and_white("test.png", "test1.png")
        invert_colors(x)
        resize_image()
        adjust_resolution()
        tess_run()
    i += 1





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
