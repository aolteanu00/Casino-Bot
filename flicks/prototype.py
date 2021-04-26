from subprocess import call
import os
import pyautogui

#CAPTURES A SCREEN GRAB OF CURRENT BALANCE
call(["screencapture", "-R305,235,90,30", "screenshot7.jpg"]) # Captures area of screen

#OCR ANALYZES SCREENGRAB AND PROVIDES A .TXT FILE INTERPRETATION IN THE SAME DIRECTORY
os.system('tesseract screenshot7.jpg --psm 6')

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
