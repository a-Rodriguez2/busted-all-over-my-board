import cv2
import numpy as np

def Detailed_Gray_Or_Invert(image, base_image):
    # calculate the average color of the image
    avg_color = np.average(image, axis=(0, 1))
    if avg_color[0] > 127 and avg_color[1] > 127 and avg_color[2] > 127:
        # majority color is white, use grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7,7), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        morph = thresh
        base_image = thresh.copy()
    else:
        # # majority color is black, invert the colors and convert to grayscale
        gray = cv2.bitwise_not(image)
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        base_image = morph.copy()
    cv2.imwrite("Processing/gray.png", morph)
    return morph, base_image

def Gray_Or_Invert(image):
    avg_color = np.average(image, axis=(0, 1))
    if avg_color[0] > 127 and avg_color[1] > 127 and avg_color[2] > 127:
        # majority color is white, use grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        # majority color is black, invert the colors and convert to grayscale
        gray = cv2.bitwise_not(image)
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Processing/gray.png", gray)
    return gray

def Blur_And_Thresh(gray):
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh


def ROI_Single(cropThresh, bottomCrop, base_image, image, thresh):
    im_h, im_w, im_d= image.shape
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 1))
    dilate = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imwrite("Processing/kernal.png", kernel)
    cv2.imwrite("Processing/dilate.png", dilate)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda y: cv2.boundingRect(y)[1])
    roi = base_image
    rect = base_image.copy()
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        rect = cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        if h/im_h > cropThresh:
            cropBottom = int((y+h)+im_h*bottomCrop)
            roi = base_image[y+h:cropBottom, 0:im_w]
    cv2.imwrite("Processing/roi.png", roi)
    cv2.imwrite("Processing/output.png", rect)
    return roi

def ROI_Double(cropThresh, firstLineCrop, secondLineStarting, secondLineCrop, base_image, image, gray):
    # Create rectangular structuring element and dilate
    im_h, im_w, im_d = image.shape
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 1))
    dilate = cv2.dilate(gray, kernel, iterations=1)
    # Find contours and draw rectangle
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda y: cv2.boundingRect(y)[1])
    rect = base_image.copy()
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        rect = cv2.rectangle(rect, (x, y), (x + w, y + h), (36,255,12), 2)

        if h/im_h > cropThresh:
            cropBottom = int((y+h)+im_h*firstLineCrop)
            starting = int((y+h)+im_h*secondLineStarting)
            cropBottomTwo = int((cropBottom+im_h*secondLineCrop))
            roiLineOne = base_image[y+h:cropBottom , 0:im_w]
            roiLineTwo = base_image[starting:cropBottomTwo, 0:im_w]
    cv2.imwrite("Processing/roi1.png", roiLineOne)
    cv2.imwrite("Processing/roi2.png", roiLineTwo)
    cv2.imwrite("Processing/output.png", rect)
    return roiLineOne, roiLineTwo

def Rotate_Image(angle, image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated
