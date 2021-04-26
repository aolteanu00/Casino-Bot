import cv2
from PIL import Image

img = cv2.imread('screenshot.jpg')
# If your image is not already grayscale :
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold = 180 # to be determined
_, img_binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
pil_img = Image.fromarray(img_binarized)
