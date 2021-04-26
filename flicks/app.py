import cv2
import pytesseract

def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text

img = cv2.imread('img.jpg')

print(ocr_core(img))
