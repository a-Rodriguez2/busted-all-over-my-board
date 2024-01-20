# dependencies
#pip install ultralytics // might need to be: pip install ultralytics == 8.0.112 I used this version

# 1 Imports
import csv
import cv2
import os
import ultralytics
from ultralytics import YOLO
import pylibdmtx.pylibdmtx as dmtx
from PIL import Image
import Algorithms
import Services
import Paths

# 2 Constant File Paths
model_path = Paths.Model_Path
captured_path = Paths.Captured_Images_Path
project_path = Paths.Results_Path
name_path = Paths.Name_Path
cropped_path = Paths.Cropped_Path
cropped_2d_data_matrix_path = Paths.Cropped_2D_Data_Matrix_Path
cropped_id_block_path = Paths.Cropped_ID_Block_Path
temp_path = Paths.Temp_Path
binary_image = Paths.Binary_Image_Name
confidence_rating = 0.21

# 3 Load the pretrained model
model = YOLO(model_path)

#4 Object Detection Functions
def Detect_All():
    # detects everything
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=True, save_crop=False, classes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

def Detect_ID_Block():
    # only detects the ID block
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=True, save_crop=False, classes=12)

def Detect_Cropped_ID_Block():
    # crops detected ID block
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=False, save_crop=True, classes=12)

def Detect_2D_Data_Matrix():
    # only detects the 2D data matrix
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=True, save_crop=False, classes=0)

def Detect_Cropped_2D_Data_Matrix():
    # crops detected 2D data matrix
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=False, save_crop=True, classes=0)

def Detect_IOPorts_CardSlots():
     # detects all of the I/O ports and card slots
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=True, save_crop=False, classes=[1,2,5,6,7,9,10,11,13,14,16,17,19])

def Detect_Defects():
    # detects only defects 
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=True, save_crop=False, classes=[3,4,8,15,18])

def Detect_Custom(choice):
    result = model.predict(source=captured_path, conf=confidence_rating, project=project_path, name=name_path, save=True, save_crop=False, classes=[choice])

def Decode_Color_Barcodes(image):
    # Decode Data Matrix barcodes
    barcodes = dmtx.decode(image)
    # Check if any barcodes were detected
    try: 
        for barcode in barcodes:
            # Extract the barcode data
            barcode_data = barcode.data.decode("utf-8")
            return True, barcode_data
        # If no barcodes are detected
    except:
        print("Color Error")
    print("Executing colored 2D data matrix recognition")
    return False, None

def Decode_Gray_Barcodes(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert the grayscale image to binary using Otsu's thresholding
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    os.chdir(Paths.Temp_Path)
    cv2.imwrite( "binary.png", binary)
    os.chdir(Paths.Home_Path)
    # Iterate over detected barcodes
    barcodes = dmtx.decode(binary)
    try:
        # Check if any barcodes were detected
        for barcode in barcodes:
            # Extract the barcode data
            barcode_data = barcode.data.decode("utf-8")
            return True, barcode_data
        # If no barcodes are detected
    except:
        print("Gray Error")
    print("Executing gray 2D data matrix recognition")
    return False, None

def Text_And_Barcode():
    error_string = ""
    data = ""
    # check if crop file exists
    if os.path.exists(cropped_path):
        # check if cropped 2d data matrix file exists
        if os.path.exists(cropped_2d_data_matrix_path):
            for filename in os.listdir(cropped_2d_data_matrix_path):
                if os.path.isfile(os.path.join(cropped_2d_data_matrix_path, filename)):
                    image = cv2.imread(cropped_2d_data_matrix_path + "/" + filename)
                    barcode_found = False
                    found, barcode_data = Decode_Color_Barcodes(image)
                    if found:
                        data = str(barcode_data)
                        barcode_found = True
                    if (barcode_found == False) or (len(data) != 23):
                        found, barcode_data = Decode_Gray_Barcodes(image)
                        if found:
                            data = str(barcode_data)
                            barcode_found = True
                        if (barcode_found == False) or (len(data) != 23):
                            error_string = "2D Data Matrix Image Found No Result"
        # check if cropped id matrix file exists
        elif os.path.exists(cropped_id_block_path):             
            for filename in os.listdir(cropped_id_block_path):
                if os.path.isfile(os.path.join(cropped_id_block_path, filename)):
                    image = cv2.imread(cropped_id_block_path + "/" + filename)
                    barcode_found = False
                    found, barcode_data = Decode_Color_Barcodes(image)
                    if found:
                        data = str(barcode_data)
                        barcode_found = True
                    if (barcode_found == False) or (len(data) != 23):
                        found, barcode_data = Decode_Gray_Barcodes(image)
                        if found:
                            data = str(barcode_data)
                            barcode_found = True         
                    if (barcode_found == False) or (len(data) != 23):
                        error_string = "Scanning ID Block Found No Result"
                        print(error_string)
                        if os.path.isfile(os.path.join(temp_path, binary_image)):
                            Binary_Image = cv2.imread(temp_path + "\\binary.png")
                            try:
                                print("Executing Algorithm 1 ")
                                data = Algorithms.Algorithm_One(Binary_Image)
                            except:
                                if (Services.Check_Pattern(data) == False) or (error_string == "Scanning ID Block Found No Result"):
                                    try:
                                        print("Executing Algorithm 2 ")
                                        data = Algorithms.Algorithm_Two(Binary_Image)
                                    except:
                                        if (Services.Check_Pattern(data) == False) or (error_string == "Scanning ID Block Found No Result"):
                                            try:
                                                print("Executing Algorithm 3 " )
                                                data = Algorithms.Algorithm_Three(Binary_Image)
                                            except:
                                                error_string = "Binary Text Recognition Found No Result"
                        if (error_string == "Binary Text Recognition Found No Result") or (len(data) != 23):     
                            if os.path.isfile(os.path.join(cropped_id_block_path, Paths.Front_Image_Name)):
                                Front_Image = cv2.imread(cropped_id_block_path + "/" + Paths.Front_Image_Name)
                                try:
                                    print("Executing Algorithm 1 " )
                                    data = Algorithms.Algorithm_One(Front_Image)
                                except:
                                    if (Services.Check_Pattern(data) == False) or (error_string == "Binary Text Recognition Found No Result"):
                                        try:
                                            print("Executing Algorithm 2 " )
                                            data = Algorithms.Algorithm_Two(Front_Image)
                                        except:
                                            if (Services.Check_Pattern(data) == False) or (error_string == "Binary Text Recognition Found No Result"):
                                                try:
                                                    print("Executing Algorithm 3 " )
                                                    data = Algorithms.Algorithm_Three(Front_Image)
                                                except:
                                                    error_string = "Front Text Recognition Found No Result"        
                            if os.path.isfile(os.path.join(cropped_id_block_path, Paths.Back_Image_Name)) and error_string == "Front Text Recognition Found No Result":
                                Back_Image = cv2.imread(cropped_id_block_path + "/" + Paths.Back_Image_Name)
                                try:
                                    print("Executing Algorithm 1 " )
                                    data = Algorithms.Algorithm_One(Back_Image)
                                except:
                                    if (Services.Check_Pattern(data) == False) or (error_string == "Binary Text Recognition Found No Result"):
                                        try:
                                            print("Executing Algorithm 2 " )
                                            data = Algorithms.Algorithm_Two(Back_Image)
                                        except:
                                            if (Services.Check_Pattern(data) == False) or (error_string == "Binary Text Recognition Found No Result"):
                                                try:
                                                    print("Executing Algorithm 3: " )
                                                    data = Algorithms.Algorithm_Three(Back_Image)
                                                except:
                                                    error_string = "Back Text Recognition Found No Result"
                        if (Services.Check_Pattern(data) == False) or (len(data) != 23):
                            data = "Process Failed: Try Manually Entering The PPID or Start Again From Image Capture"
                        else:
                            print(data)
                            data = data.replace("-", "")
        else:
            data = "Cropped Image Was Not Found"

    if (os.path.isfile((os.path.join(Paths.Temp_Path, Paths.Binary_Image_Name)))):
        os.remove(os.path.join(Paths.Temp_Path, Paths.Binary_Image_Name))
    
    return data

def Write_Report(StationNumber, WorkID, FoundPPID, ReportName):
    report = [ ['Station Number', StationNumber],
               ['Work ID', WorkID],
               ['PPID', FoundPPID],
             ]
    with open(ReportName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(report)
