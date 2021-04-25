import pyscreenshot as ImageGrab
import pytesseract
import pyautogui
import time
from pynput.keyboard import Key, Controller

#setting default values
previous_balance = 0
previous_bet = 0.01

#take a screen shot and extracts the balance from image to a float
def get_balance():
    #screen shot function with (x1, y1, x2, y2) being coordinates of the balance @ CSGO roll
    image = ImageGrab.grab(bbox=(2049, 116, 2110, 152))
    image.save('E:\Python Project\Screen_shots\screenshot1.png')

    pytesseract.pytesseract.tesseract_cmd = r'E:\Python Project\tesseract\tesseract'
    balance = pytesseract.image_to_string(r'E:\Python Project\Screen_shots\screenshot1.png')
    return balance


#function to clear the betting area of previous bets
def betting():
    # click into the betting box @CSGO roll
    pyautogui.click(844, 678)

    # deletes anything in the betting box up to 10 characters long
    keyboard = Controller()
    for i in range(10):
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

#function to run the code every 23 seconds (time it takes CSGO roll to reset round)
def timer():
    global previous_balance
    global previous_bet

    #gets the balance from CSGO roll
    current_balance = get_balance()
    print(current_balance)
    #converting balance to a float
    float_previous_balance = float(previous_balance)

    #if the current balance > the previous balance = you won
    if float(current_balance) >= float_previous_balance:
        print("win")
        #winning = place default bet number
        betting()
        keyboard = Controller()
        keyboard.type("0.01")
        previous_bet = 0.01
        previous_balance = current_balance
    #if the current balance < the previous balance = you lost
    elif float(current_balance) < float_previous_balance:
        print("lose")
        pyautogui.click(2225, 669)
        #losing = place double the previous bet
        previous_bet = previous_bet * 2
        previous_balance = current_balance

    #clicks the bet button
    pyautogui.click(2193, 804)
    time.sleep(23)


while True:
    timer()
