import pyscreenshot
import time

x=1
while x<2:
    image = pyscreenshot.grab(bbox=(303, 392, 235, 235))

    image.show()
    image.save('/Users/dominicesposito/Desktop/Screenshots')
    x+=1
    time.sleep(2)
    print('Done')
