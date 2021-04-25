import pyscreenshot as ImageGrab
import pytesseract
import pyautogui
import time




pytesseract.pytesseract.tesseract_cmd = r'E:\Python Project\tesseract\tesseract'
balance = pytesseract.image_to_string(r'/Users/alexolteanu/Desktop/Bot/flicks/screenshot.jpg')
print(balance)
