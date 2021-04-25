import pyautogui
print(pyautogui.position())

#re-bet coordinates: (1154,544)
#pyautogui.click(x=1154, y=5444, clicks=1, interval=20, button='left')
pyautogui.click(x=1154, y=544, clicks=1, button='left')
pyautogui.click(x=1154, y=544, clicks=1, button='left')
pyautogui.click()

x = 0
while x < 10:
    pyautogui.click(x=1154, y=544, clicks=1, button='left')
    pyautogui.click(x=1154, y=544, clicks=1, button='left')
    pyautogui.click(interval = 7)
    x+=1
