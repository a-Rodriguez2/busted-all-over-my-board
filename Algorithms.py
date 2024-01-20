import cv2
import pytesseract
import numpy as np
import re
from AlgorithmServices import Gray_Or_Invert, Blur_And_Thresh, ROI_Single, Detailed_Gray_Or_Invert, ROI_Double, Rotate_Image

def Algorithm_One(main_image):
    image = main_image.copy()
    base_image = image.copy()
    gray = Gray_Or_Invert(image)
    thresh = Blur_And_Thresh(gray)
    roi = ROI_Single(0.32, 0.25, base_image, image, thresh)
    ocr_result_original = pytesseract.image_to_string(roi)
    return ocr_result_original

def Algorithm_Two(main_image):
    image = main_image.copy()
    base_image = image.copy()
    gray, base_image = Detailed_Gray_Or_Invert(image, base_image)
    roiLineOne, roiLineTwo = ROI_Double(0.32, 0.13, 0.13, 0.109, base_image, image, gray)
    ocrLineOne = pytesseract.image_to_string(roiLineOne)
    ocrLineTwo = pytesseract.image_to_string(roiLineTwo)
    response = ocrLineOne+ocrLineTwo
    return(response)

def Algorithm_Three(main_image):
    image = main_image.copy()
    base_image = image.copy()
    gray, base_image = Detailed_Gray_Or_Invert(image, base_image)
    base_image = Rotate_Image(1, base_image)
    roiLineOne, roiLineTwo = ROI_Double(0.32, 0.13, 0.126, 0.11, base_image, image, gray)
    ocrLineOne = pytesseract.image_to_string(roiLineOne)
    ocrLineTwo = pytesseract.image_to_string(roiLineTwo)
    response = ocrLineOne+ocrLineTwo
    return(response)