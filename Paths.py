"""
Directory Hierarchy
> Home (or Project)
    > Captured
        > Back.png
        > Front.png
    > Extra
        > ...
    > Model
        > best.py
    > Reports
        > Report 1
        > Report 2
        > Report 3
        ...
    > Results
        > Run
            > Back.png
            > Front.png
            > cropped
                2D DataMatrix
                    > ...
                ID
                    > ...
    > temp
        > ...
    > Tests
        > Test 1
        > Test 2
        > Test 3
        ...

    ## Python Files
    Detection.py
    Icons_rc.py
    LayoutGUI.py
    MainGUI.py
    Paths.py
    ...
"""

# In the ultralytics source code, cropped images are saved in the jpg format. To change this to the png format, the file called "plotting.py"
# in the path ...\ultralytics\yolo\utils\plotting.py needs to be modified. In the file "plotting.py", the two hard coded ".jpg" in the function 
# "save_one_box" need to be changed to ".png" to change the cropped images format.

import os

# Front image name and format
Front_Image_Name = r'Front.png'

# Back image name and fromat
Back_Image_Name = r'Back.png'
#####ONLY PATH YOU NEED TO UPDATE IS BELOW HERE
# Path to the project home directory (or simply the project file: r'.\Project')
Home_Path = r'C:\Users\farid\OneDrive\Desktop\Fall2023\Senior Design\motherboard_identification_and_image_capture-main'

#put your path main folder here ^^^


# Path to the file where the custom model is held.
# Model_Path = r'.\Model\best.pt' 
Model_Path = os.path.join(Home_Path, "Model", "best.pt")

# Path to the file where the captured images are held.
# Captured_Images_Path = r'.\Captured'
Captured_Images_Path = os.path.join(Home_Path, "Captured")

# Path to latest captured front image.
# Front_Image_Path = r'.\Captured\Front.jpg'
Front_Image_Path = os.path.join(Captured_Images_Path, Front_Image_Name)

# Path to latest captured back image.
# Back_Image_Path = r'.\Captured\Back.jpg'
Back_Image_Path = os.path.join(Captured_Images_Path, Back_Image_Name)

# Path to the file were the results will be placed, the Run folders will be placed as a sub directory of Results.
# Results_Path = r'.\Results'
Results_Path = os.path.join(Home_Path, "Results")

# This is the general name of the sub directory the results will be saved into.
# The results be saved in the path: .\Results\Run#, the # indicates the instance the program was launched under.
# Each time the program is ran and a result is produced, the # in Run# will increment by 1 and the results will be saved there in the new folder.
# The results for the first instance is always named Run, the results for the second instance is named Run2 and so on...
Name_Path = os.path.join(Results_Path, "Run2")
# Path to detected images
# Detected_Path = r'.\Results\Run'
Detected_Path = os.path.join(Results_Path, "Run")

# Path to latest front image after detection.
# Detected_Front_Path = r'.\Results\Run\Front.jpg'
Detected_Front_Path = os.path.join(Detected_Path, Front_Image_Name)

# Path to latest back image after detection.
# Detected_Back_Path = r'.\Results\Run\Back.jpg'
Detected_Back_Path = os.path.join(Detected_Path, Back_Image_Name)

# Path to cropped images directories
# Cropped_Path = r'.\Results\Run\crops'
Cropped_Path = os.path.join(Detected_Path, "crops")

# Path to latest cropped 2D Data Matrix image.
# Cropped_2D_Data_Matrix_Path = r'.\Results\Run\crops\2D DataMatrix'
Cropped_2D_Data_Matrix_Path = os.path.join(Cropped_Path, "2D DataMatrix")

# Path to latest cropped ID Block image.
# Cropped_ID_Block_Path = r'.\Results\Run\crops\ID'
Cropped_ID_Block_Path = os.path.join(Cropped_Path, "ID")

# Path to where the test files are stored.
# Test_Files_Path = r'.\Tests'
Test_Files_Path = os.path.join(Home_Path, "Tests")

# Path to where the Report files are stored.
# Report_Files_Path = r'.\Reports'
Report_Files_Path = os.path.join(Home_Path, "Reports")

# Path to the temp file used for text recognition
Temp_Path = os.path.join(Home_Path, "Processing")

# Path to where the binary image is stored for text recognition
Binary_Image_Name = r'binary.png'

# FTP Host Name, Username, and Password
Host_Name = r'10.159.40.187'
Host_Username = r'sms'
Host_Password = r'UTDesign1675'
Host_CWD = r'Reports'
