import pytesseract
from PIL import Image
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

file_path= 'anpr_detection/license-plates/AM74043-update.jpg'
im = Image.open(file_path)
im.save('anpr_detection/ocr.png', dpi=(300, 300))

image = cv2.imread('anpr_detection/ocr.png')
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

retval, threshold = cv2.threshold(image,110,255,cv2.THRESH_BINARY_INV)

text = pytesseract.image_to_string(threshold)

with open('Output.txt', 'w',5 ,'utf-8') as text_file:
    text_file.write(text)

print(text)