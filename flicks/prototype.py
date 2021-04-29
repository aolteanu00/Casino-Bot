from subprocess import call
import os
import pyautogui
from PIL import Image
import PIL.ImageOps
import time
import random

print("*")
print("*")
print("*")
print("DRIPBOT IS LIVE")
print("_________________________________________________________________________")
list = ["z", 'x']
#num_loss = 0
time_list = [14.6, 14.7, 14.8, 14.9, 15.1, 15.1, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9]

#pyautogui functions
def chip():
    pyautogui.click(x=691, y=887, clicks=1, button='left')
    pyautogui.click(x=691, y=887, clicks=1, button='left')

def player():
    pyautogui.click(x=714, y=613, clicks=1, button='left')
    pyautogui.click(x=714, y=613, clicks=1, button='left')

def deal():
    pyautogui.click(x=1564, y=616, clicks=1, interval=2, button='left')
    pyautogui.click(x=1564, y=616, clicks=1, interval=2, button='left')

def re_bet():
    pyautogui.click(x=1560, y=528, clicks=2, button='left')
    pyautogui.click(x=1560, y=528, clicks=2, button='left')

def re_bet2x():
    pyautogui.click(x=1561, y=703, clicks=2, button='left')
    pyautogui.click(x=1561, y=703, clicks=2, button='left')

#image functions
def screengrab():
    call(["screencapture", "-R390,280,150,50", "test.jpg"])
    image = Image.open('test.jpg')
    new_image = image.resize((250, 50))
    new_image.save("test.png")


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

#tesseract function
def tess_run():
    os.system("tesseract test4.png tess 6")
    file_in = open('tess.txt', 'r')
    y = file_in.read().split(',')
    w = ''.join(y)
    r = w.replace('\n\x0c', '')
    q = float(r)
    z = list.append(q)


#bet
def bet():
    all_in = 0
    if all_in == 9:
        pyautogui.click(x=1128, y=892, clicks=1, button='left')
        player()
        deal()
        list.pop(-3)
    if list[-1] > list[-2]:
        player()
        deal()
        all_in = 0
        list.pop(-3)
        #num_loss = 0
    if list[-1] < list[-2]:
        re_bet2x()
        all_in += 1
        list.pop(-3)
        #num_loss = num_loss + 1

    else:
        re_bet()
        list.pop(-3)



def image_func():
    screengrab()
    x = black_and_white("test.png", "test1.png")
    invert_colors(x)
    resize_image()
    adjust_resolution()
    tess_run()


def start_game():
    image_func()
    chip()
    player()
    deal()
    list.pop(-3)
    time.sleep(8)

def body():
    image_func()
    bet()




i = 0
while i < 1:
    start_game()
    i += 1
i2 = 0
while i2 < 7200:
    body()
    i2 += 1
    print(list)
    x = random.choice(time_list)
    time.sleep(x)



print("_________________________________________________________________________")
print("DRIPBOT OUT")
print("*")
print("*")
print("*")
