import os
import cv2
import glob
import shutil
import tkinter as tk
import ftplib
from datetime import datetime
from LayoutGUI import *
import Paths
import Detection

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ### Button Connections
        ## Window Flags
        # Removes Default Window Flags
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Custom Window Flag Connections
        self.ui.Close_B.clicked.connect(lambda: self.close())
        self.ui.Exit_B.clicked.connect(lambda: self.close())
        self.ui.Maximize_B.clicked.connect(lambda: self.Restore_Or_Maximize_Window())
        self.ui.Minimize_B.clicked.connect(lambda: self.showMinimized())
        # Custom Window Size Grip Connection
        QtWidgets.QSizeGrip(self.ui.Size_Grip)

        ## Move Window By Dragging Window Header Connection
        self.ui.Header_Container.mouseMoveEvent = self.Move_Window
        self.ui.Header_Container.mousePressEvent = self.Mouse_Press

        ## Open and Close Slide Menu Connection
        self.ui.Open_Slide_B.clicked.connect(lambda: self.Slide_Left_Menu())

        ## Slide Menu Button Connections
        # Home Sub Page 1
        self.ui.Home_1A.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        # Capture Images Page
        self.ui.Image_Capture_Take_1B.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        # Normal Detection Page
        self.ui.Detection_Normal_1B.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        # Custom Detection Page
        self.ui.Detection_Custom_2B.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        # Matrix Detectection Page
        self.ui.Detection_Matrix_3B.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        # Testing Sub Page 1
        self.ui.Testing_1B.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(5))

        ## Change Pages Using Footer Button Connections
        # Go To Previous Page
        self.ui.Previous_Page_B.clicked.connect(lambda: self.Previous_Page())
        # Go To Next Page
        self.ui.Next_Page_B.clicked.connect(lambda: self.Next_Page())

        ## Identification Page Connections
        # Save Station Number Button Connection
        self.ui.Station_Number_Save_B.clicked.connect(lambda: self.Save_Station_Number())
        # Save Work ID Button Connection
        self.ui.Work_ID_Save_B.clicked.connect(lambda: self.Save_Work_ID())

        ## Image Capture Page Connections
        # Instantiate A Thread
        self.ImageCapture = ImageCapture()
        # Retrive A Converted Frame
        self.ImageCapture.start()
        # Update The Lable With The New Converted Frame
        self.ImageCapture.ImageUpdate.connect(self.Image_Update_Slot)
        # Raise Capture Front Image Flag
        self.ui.Capture_Front_B.clicked.connect(self.ImageCapture.Capture_Front)
        # Raise Capture Back Image Flag
        self.ui.Capture_Back_B.clicked.connect(self.ImageCapture.Capture_Back)
        # Show Front Captured Image In Window
        self.ImageCapture.UpdateCapturedFront.connect(self.Captured_Front_Image)
        # Show Back Captured Image In Window
        self.ImageCapture.UpdateCapturedBack.connect(self.Captured_Back_Image)
        # View Front Captured Image In Separate Window
        self.ui.View_Front_B.clicked.connect(lambda: self.View_Front())
        # View Back Captured Image In Separate  Window
        self.ui.View_Back_B.clicked.connect(lambda: self.View_Back())

        ## Normal Detection Page Connections
        # Detect Everything
        self.ui.Detect_All_B.clicked.connect(lambda: self.Normal_Detection_All())
        # Detect ID Block
        self.ui.Detect_ID_Block_B.clicked.connect(lambda: self.Normal_Detection_ID_Block())
        # Detect 2D Data Matrix
        self.ui.Detect_2D_Data_Matrix_B.clicked.connect(lambda: self.Normal_Detection_2D_Data_Matrix())
        # Detect IO Ports And Card Slots
        self.ui.Detect_IOPorts_CardSlots_B.clicked.connect(lambda: self.Normal_Detection_IOPorts_CardSlots())
        # Detect Defects
        self.ui.Detect_Defects_B.clicked.connect(lambda: self.Normal_Detection_Defects())
        # See All Images
        self.ui.See_N_Detected_Images_B.clicked.connect(lambda: self.See_Normal_Detection_Page_Images())
        
        ## Custom Detection Page Connections
        # Perform Custom Detection
        self.ui.Run_C_Detection_B.clicked.connect(lambda: self.Custom_Detection())
        # Check All Boxes
        self.ui.Check_All_B.clicked.connect(lambda: self.Check_All())
        # Check All Boxes
        self.ui.Uncheck_All_B.clicked.connect(lambda: self.Uncheck_All())
        # View Images Before Custom Detection
        self.ui.View_Before_C_Detection_B.clicked.connect(lambda: self.See_Custom_Detection_Before_Images())
        # View Images After Custom Detection
        self.ui.View_After_C_Detection_B.clicked.connect(lambda: self.See_Custom_Detection_After_Images())

        ## 2D Matrix Recognition Page Connections
        # Perform Recognition On The Detected 2D Data Matrix Or ID Block Connection
        self.ui.Run_Recognition_B.clicked.connect(lambda: self.Perform_Recognition())
        # Save Recognition Results
        self.ui.Save_Results_B.clicked.connect(lambda: self.Save_Recognition_Results())
        # Save Manually Entered PPID Button Connection
        self.ui.PPID_Save_B.clicked.connect(lambda: self.Save_PPID())

        ## Test and Report Page Connections
        # Select Test File Connection 
        self.ui.Choose_Test_File_B.clicked.connect(lambda: self.Select_Test_File())
        # Run Test File Connection 
        self.ui.Run_Test_File_B.clicked.connect(lambda: self.Execute_Test_File())
        # Generate Report Connection 
        self.ui.Generate_Report_B.clicked.connect(lambda: self.Make_Report())
        # View Generated Report Connection 
        self.ui.View_Report_B.clicked.connect(lambda: self.See_Report())
        # Send Generated Report Connection 
        self.ui.Send_Report_B.clicked.connect(lambda: self.Send_Report())

        ## Variables Used To Hold User Input
        self.Current_Station_Number = ""
        self.Current_Work_ID = ""
        self.Current_PPID = ""
        self.Current_Test_File = ""
        self.Current_Report_File = ""

    ## Close Main Window And Open Image Viewer Window Function
    def Show_Image_Viewer(self):
        image_window.setFocus()
        image_window.show()

    ## Maximize And Minimize Window Function
    def Restore_Or_Maximize_Window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.Maximize_B.setIcon(QtGui.QIcon(u":/Icons/Icons2/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.Maximize_B.setIcon(QtGui.QIcon(u":/Icons/Icons2/minimize-2.svg"))
    
    ## Click And Drag Window Using Header Functions
    # Register Click On The Header Function
    def Mouse_Press(self, event):
            self.dragPos = self.pos()
            self.mouse_original_pos = self.mapToGlobal(event.pos())
            
    # Move The Window Function
    def Move_Window(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                MainWindow_last_pos = self.dragPos + self.mapToGlobal(event.pos()) - self.mouse_original_pos
                self.move(MainWindow_last_pos)
                event.accept()

    ## Open And Close Slide Menu Function
    def Slide_Left_Menu(self):
        width = self.ui.Slide_Menu_Container.width()
        if width == 0:
            newWidth = 200
            self.ui.Open_Slide_B.setIcon(QtGui.QIcon(u":/Icons/Icons2/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.Open_Slide_B.setIcon(QtGui.QIcon(u":/Icons/Icons2/menu.svg"))
        self.animation = QtCore.QPropertyAnimation(self.ui.Slide_Menu_Container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    ## Change Page Using Footer Buttons Functions
    # View Previous Page Function
    def Previous_Page(self):
        Current_Index = self.ui.stackedWidget.currentIndex()
        if Current_Index == 0:
            self.ui.stackedWidget.setCurrentIndex(5)
        else:
            self.ui.stackedWidget.setCurrentIndex(Current_Index - 1)

    # View Next Page Function
    def Next_Page(self):
        Current_Index = self.ui.stackedWidget.currentIndex()
        if Current_Index == 5:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(Current_Index + 1)

    ## Identification Page Functions
    # Save Station Number Function
    def Save_Station_Number(self):
        self.ui.Saved_Station_Number_L.setText(f'Saved Station Number: {self.ui.Station_Number_LE.text()}')
        self.ui.Station_Number_Result_L.setText(f'Saved Station Number: {self.ui.Station_Number_LE.text()}')
        self.Current_Station_Number = str(self.ui.Station_Number_LE.text())

    # Save Work ID Function
    def Save_Work_ID(self):
        self.ui.Saved_Work_ID_L.setText(f'Saved Work ID: {self.ui.Work_ID_LE.text()}')
        self.ui.Work_ID_Result_L.setText(f'Saved Work ID: {self.ui.Work_ID_LE.text()}')
        self.Current_Work_ID = str(self.ui.Work_ID_LE.text())
    
    ## Captured Images Page Functions
    # Update Live Feed For Image Capture Function
    def Image_Update_Slot(self, Image):
        self.ui.Live_Video_L.setPixmap(QtGui.QPixmap.fromImage(Image))

    # Show Captured Front Image Function
    def Captured_Front_Image(self, Image):
        self.ui.PPID_Recogniton_L.setText(f'PPID: ')
        self.ui.PPID_LE.clear()
        self.ui.Saved_PPID_L.setText(f'Saved PPID: ')
        self.ui.PPID_Result_L.setText(f'Saved PPID: ')
        self.ui.Front_Image_L.setPixmap(QtGui.QPixmap.fromImage(Image))
        self.ui.Front_Before_N_Detection_L.setPixmap(QtGui.QPixmap.fromImage(Image))
        self.ui.Front_Before_C_Detection_L.setPixmap(QtGui.QPixmap.fromImage(Image)) 

    # Show Captured Back Image Function
    def Captured_Back_Image(self, Image):
        self.ui.PPID_Recogniton_L.setText(f'PPID: ')
        self.ui.PPID_LE.clear()
        self.ui.Saved_PPID_L.setText(f'Saved PPID: ')
        self.ui.PPID_Result_L.setText(f'Saved PPID: ')
        self.ui.Back_Image_L.setPixmap(QtGui.QPixmap.fromImage(Image))
        self.ui.Back_Before_N_Detection_L.setPixmap(QtGui.QPixmap.fromImage(Image))
        self.ui.Back_Before_C_Detection_L.setPixmap(QtGui.QPixmap.fromImage(Image))
            
    # View Front Captured Image In New Window Function
    def View_Front(self):
        if len(os.listdir(Paths.Captured_Images_Path)) != 0:  
            os.startfile(Paths.Front_Image_Path)
        else:
            self.Show_Popup()

    # View Back Captured Image In New Window Function
    def View_Back(self):
        if len(os.listdir(Paths.Captured_Images_Path)) != 0:
            os.startfile(Paths.Back_Image_Path)
        else:
            self.Show_Popup()

    # Popup Message If No Captured Image Is Found Function
    def Show_Popup(self):
        msg = QtWidgets.QMessageBox()   
        msg.setWindowTitle("Error")
        msg.setText("Image Was Not Found!")
        msg.setDetailedText("The Images Were Not Found In File. Try Again From The Start")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        msg.setFont(font)
        msg.setStyleSheet("QMessageBox {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "}\n"
        "\n"
        "QMessageBox QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    background-color: rgb(0,122,204);\n"
        "    border-radius: 5px;\n"
        "    padding: 10px;\n"
        "}\n"
        "\n"
        "QMessageBox QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}"
        "QMessageBox QLabel {\n"
        "    color:rgb(167, 167, 167);\n"
        "}")
        msg.exec_()

    ## Normal Detection Page Functions
    def Detection_Check(self):
        os.chdir(Paths.Home_Path)
        if os.path.exists(Paths.Cropped_Path):
            shutil.rmtree(Paths.Cropped_Path)
        if os.path.exists(Paths.Detected_Path):
            shutil.rmtree(Paths.Detected_Path)

    def Normal_Detection_All(self):
        self.Detection_Check()
        Detection.Detect_All()
        self.Show_Detected_Images()

    def Normal_Detection_ID_Block(self):
        self.Detection_Check()
        Detection.Detect_ID_Block()
        Detection.Detect_Cropped_ID_Block()
        self.Show_Detected_Images()
        self.Show_2D_Data_Matrix_Or_ID_Block()

    def Normal_Detection_2D_Data_Matrix(self):
        self.Detection_Check()
        Detection.Detect_2D_Data_Matrix()
        Detection.Detect_Cropped_2D_Data_Matrix()
        self.Show_Detected_Images()
        self.Show_2D_Data_Matrix_Or_ID_Block()
    
    def Normal_Detection_IOPorts_CardSlots(self):
        self.Detection_Check()
        Detection.Detect_IOPorts_CardSlots()
        self.Show_Detected_Images()
    
    def Normal_Detection_Defects(self):
        self.Detection_Check()
        Detection.Detect_Defects()
        self.Show_Detected_Images()

    # See Images After Normal Detection In New Window Function
    def See_Normal_Detection_Page_Images(self):
        ImagePaths = []
        if os.path.exists(Paths.Captured_Images_Path):
            Path = Paths.Captured_Images_Path
            if len(os.listdir(Path)) != 0:
                for x in os.listdir(Path):
                    if os.path.isfile(os.path.join(Path, x)):
                        ImagePaths.append(str(Path) + "\\" + str(x))
            else:
                self.Show_Popup()
        else:
            pass
        if os.path.exists(Paths.Detected_Path):
            Path = Paths.Detected_Path
            if len(os.listdir(Path)) != 0:
                for x in os.listdir(Path):
                    if os.path.isfile(os.path.join(Path, x)):
                        ImagePaths.append(str(Path) + "\\" + str(x))
            else:
                self.Show_Popup()
        else:
            pass
        if len(ImagePaths) == 4:
            ImagePaths[1], ImagePaths[2] = ImagePaths[2], ImagePaths[1]
        self.Open_Image_Viewer(ImagePaths)
        
    ## Open Image Viewer And Send Image Paths Function
    def Open_Image_Viewer(self, image_paths):
        ImagePaths = image_paths
        if len(image_paths) != 0:
            image_window.Get_Image_Paths(ImagePaths)
            self.Show_Image_Viewer()

    # Show Images After Normal Detection Function
    def Show_Detected_Images(self):
        if os.path.exists(Paths.Detected_Path):
            if os.path.isfile(os.path.join(Paths.Detected_Path, Paths.Front_Image_Name)):
                img = cv2.imread(os.path.join(Paths.Detected_Path, Paths.Front_Image_Name), cv2.IMREAD_UNCHANGED)
                FrontImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                FrontImageConvertToQtFormat = QtGui.QImage(FrontImage.data, FrontImage.shape[1], FrontImage.shape[0], QtGui.QImage.Format_RGB888)
                FrontPicture = FrontImageConvertToQtFormat.scaled(400, 300, QtCore.Qt.KeepAspectRatio)       
                self.ui.Front_After_N_Detection_L.setPixmap(QtGui.QPixmap.fromImage(FrontPicture))
            else:
                self.ui.Front_After_N_Detection_L.clear()
                self.ui.Front_After_N_Detection_L.setText("Image Not Found")
            if os.path.isfile(os.path.join(Paths.Detected_Path, Paths.Back_Image_Name)):
                img = cv2.imread(os.path.join(Paths.Detected_Path, Paths.Back_Image_Name), cv2.IMREAD_UNCHANGED)               
                BackImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                BackImageConvertToQtFormat = QtGui.QImage(BackImage.data, BackImage.shape[1], BackImage.shape[0], QtGui.QImage.Format_RGB888)
                BackPicture = BackImageConvertToQtFormat.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
                self.ui.Back_After_N_Detection_L.setPixmap(QtGui.QPixmap.fromImage(BackPicture))
            else:
                self.ui.Back_After_N_Detection_L.clear()
                self.ui.Back_After_N_Detection_L.setText("Image Not Found")
        else:
            self.ui.Front_After_N_Detection_L.clear()
            self.ui.Front_After_N_Detection_L.setText("Image Not Found")
            self.ui.Back_After_N_Detection_L.clear()
            self.ui.Back_After_N_Detection_L.setText("Image Not Found")

    ## Custom Detection Page Functions
    # Check Boxes And Run Custom Detection Function
    def Custom_Detection(self):
        self.Detection_Check()
        checked_checkboxes = []
        checkbox = 0
        for x in range(0, self.ui.gridLayout_3.rowCount()):
            for y in range(0, self.ui.gridLayout_3.columnCount()):
                if self.ui.gridLayout_3.itemAtPosition(x, y).widget().isChecked():
                    checked_checkboxes.append(checkbox)
                checkbox += 1
        Detection.Detect_Custom(checked_checkboxes)
        self.Show_Custom_Detected_Images()
        
    # Show Images After Custom Detection Function
    def Show_Custom_Detected_Images(self):
        if os.path.exists(Paths.Detected_Path):
            if os.path.isfile(os.path.join(Paths.Detected_Path, Paths.Front_Image_Name)):
                img = cv2.imread(os.path.join(Paths.Detected_Path, Paths.Front_Image_Name), cv2.IMREAD_UNCHANGED)               
                FrontImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                FrontImageConvertToQtFormat = QtGui.QImage(FrontImage.data, FrontImage.shape[1], FrontImage.shape[0], QtGui.QImage.Format_RGB888)
                FrontPicture = FrontImageConvertToQtFormat.scaled(400, 300, QtCore.Qt.KeepAspectRatio)       
                self.ui.Front_After_C_Detection_L.setPixmap(QtGui.QPixmap.fromImage(FrontPicture))
            else:
                self.ui.Front_After_C_Detection_L.clear()
                self.ui.Front_After_C_Detection_L.setText("Image Not Found")
            if os.path.isfile(os.path.join(Paths.Detected_Path, Paths.Back_Image_Name)):
                img = cv2.imread(os.path.join(Paths.Detected_Path, Paths.Back_Image_Name), cv2.IMREAD_UNCHANGED)               
                BackImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                BackImageConvertToQtFormat = QtGui.QImage(BackImage.data, BackImage.shape[1], BackImage.shape[0], QtGui.QImage.Format_RGB888)
                BackPicture = BackImageConvertToQtFormat.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
                self.ui.Back_After_C_Detection_L.setPixmap(QtGui.QPixmap.fromImage(BackPicture))
            else:
                self.ui.Back_After_C_Detection_L.clear()
                self.ui.Back_After_C_Detection_L.setText("Image Not Found")
        else:
            self.ui.Front_After_C_Detection_L.clear()
            self.ui.Front_After_C_Detection_L.setText("Image Not Found")
            self.ui.Back_After_C_Detection_L.clear()
            self.ui.Back_After_C_Detection_L.setText("Image Not Found")

    # Chcek All Boxes Function
    def Check_All(self):
        for x in range(0, self.ui.gridLayout_3.count()):
            self.ui.gridLayout_3.itemAt(x).widget().setChecked(True)

    # Uncheck All Boxes Function
    def Uncheck_All(self):
        for x in range(0, self.ui.gridLayout_3.count()):
            self.ui.gridLayout_3.itemAt(x).widget().setChecked(False)

    # See Images Before Custom Detection In New Window Function
    def See_Custom_Detection_Before_Images(self):
        if os.path.exists(Paths.Captured_Images_Path):
            ImagePaths = []
            Path = Paths.Captured_Images_Path
            if len(os.listdir(Path)) != 0:
                for x in os.listdir(Path):
                    ImagePaths.append(str(Path) + "\\" + str(x))
                self.Open_Image_Viewer(ImagePaths)
            else:
                self.Show_Popup()
        else:
            self.Show_Popup()

    # See Images After Custom Detection In New Window Function
    def See_Custom_Detection_After_Images(self):
        if os.path.exists(Paths.Detected_Path):
            ImagePaths = []
            Path = Paths.Detected_Path
            if len(os.listdir(Path)) != 0:
                for x in os.listdir(Path):
                    ImagePaths.append(str(Path) + "\\" + str(x))
                self.Open_Image_Viewer(ImagePaths)
            else:
                self.Show_Popup()
        else:
            self.Show_Popup()

    ## 2D Matrix Recogniton Page Functions
    # Show Detected 2D Data Matrix Or ID Block After Normal Detection Function
    def Show_2D_Data_Matrix_Or_ID_Block(self):
        if os.path.exists(Paths.Cropped_ID_Block_Path):
            if os.path.isfile(os.path.join(Paths.Cropped_ID_Block_Path, Paths.Front_Image_Name)):
                self.ui.Matrix_Image_L.setPixmap(QtGui.QPixmap(os.path.join(Paths.Cropped_ID_Block_Path, Paths.Front_Image_Name)))
            else:
                self.ui.Matrix_Image_L.setPixmap(QtGui.QPixmap(os.path.join(Paths.Cropped_ID_Block_Path, Paths.Back_Image_Name)))
        elif os.path.exists(Paths.Cropped_2D_Data_Matrix_Path):
            if os.path.isfile(os.path.join(Paths.Cropped_2D_Data_Matrix_Path, Paths.Front_Image_Name)):
                self.ui.Matrix_Image_L.setPixmap(QtGui.QPixmap(os.path.join(Paths.Cropped_2D_Data_Matrix_Path, Paths.Front_Image_Name)))
            else:
                self.ui.Matrix_Image_L.setPixmap(QtGui.QPixmap(os.path.join(Paths.Cropped_2D_Data_Matrix_Path, Paths.Back_Image_Name)))
        else:
            pass

    # Perform Recognition On 2D Data Matrix
    def Perform_Recognition(self):
        self.Current_PPID = Detection.Text_And_Barcode()
        self.ui.PPID_Recogniton_L.setText(f'PPID: {self.Current_PPID}')

    # Save Recognized PPID Function
    def Save_Recognition_Results(self):
        self.ui.PPID_Recogniton_L.setText(f'PPID: {self.Current_PPID}')
        self.ui.Saved_PPID_L.setText(f'Saved PPID: {self.Current_PPID}')
        self.ui.PPID_LE.clear()
        self.ui.PPID_Result_L.setText(f'PPID: {self.Current_PPID}')
        ppid = str(self.ui.PPID_Recogniton_L.text())
        self.Current_PPID = ppid[6:]
    
    # Save Manually Entered PPID Function
    def Save_PPID(self):
        self.ui.Saved_PPID_L.setText(f'Saved PPID: {self.ui.PPID_LE.text()}')
        self.ui.PPID_Recogniton_L.setText(f'PPID: ')
        self.ui.PPID_Result_L.setText(f'Saved PPID: {self.ui.PPID_LE.text()}')
        self.Current_PPID = str(self.ui.PPID_LE.text())

    ## Test and Report Page Functions
    # Select A Test File Functon
    def Select_Test_File(self):
        Test_File = QtWidgets.QFileDialog.getOpenFileName(None, "Select Test File", Paths.Test_Files_Path, "All Files (*);;Python Files (*.py)")
        if Test_File:
            self.ui.Test_File_Name_L.setText(Test_File[0])
            self.Current_Test_File = Test_File[0]
    
    # Run Choosen Test File Function
    def Execute_Test_File(self):
        os.startfile(self.Current_Test_File)
    
    # Make A Report Function
    def Make_Report(self):
        report_name = f'{self.Current_Station_Number}_{self.Current_Work_ID}_{self.Current_PPID}_{datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")}.csv'
        os.chdir(Paths.Report_Files_Path)
        Detection.Write_Report(self.Current_Station_Number, self.Current_Work_ID, self.Current_PPID, report_name)
        os.chdir(Paths.Home_Path)
        self.Current_Report_File = os.path.join(Paths.Report_Files_Path, report_name)
    
    # View The Report Function
    def See_Report(self):
        if (len(os.listdir(Paths.Report_Files_Path)) != 0) & (os.path.isfile(self.Current_Report_File)):
            FilePath = str(Paths.Report_Files_Path)
            List_of_Files = glob.glob(str(FilePath + "\*"))
            File = max(List_of_Files, key = os.path.getctime)
            self.Current_Test_File = File
            os.startfile(File)
        else:
            self.Show_Popup()
            return

    def Send_Report(self):
        # ftps = FTP_TLS(host = Paths.Host_Name, user = Paths.Host_Username, passwd = Paths.Host_Password)
        """
        ftps = ftplib.FTP_TLS()
        ftps.connect(Paths.Host_Name)
        ftps.login(Paths.Host_Username, Paths.Host_Password)
        """
        ftps = ftplib.FTP()
        ftps.connect(Paths.Host_Name)
        ftps.login(Paths.Host_Username, Paths.Host_Password)
        ftps.cwd(Paths.Host_CWD)
        if os.path.isfile(self.Current_Report_File):
            filename = self.Current_Report_File # Need to edit this to make unique file name
            with open(filename, "rb") as file:
                ftps.storbinary('STOR ' + os.path.basename(filename), file)
        else:
            self.Show_Popup()
        ftps.quit()
        ftps.close()

        for filename in os.listdir(Paths.Captured_Images_Path):
            file_path = os.path.join(Paths.Captured_Images_Path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                print("File deletion rror")

        self.ui.Front_Image_L.clear()
        self.ui.Back_Image_L.clear()
        self.ui.Front_Before_N_Detection_L.clear()
        self.ui.Back_Before_N_Detection_L.clear()
        self.ui.Front_After_N_Detection_L.clear()
        self.ui.Back_After_N_Detection_L.clear()
        self.ui.Front_Before_C_Detection_L.clear()
        self.ui.Back_Before_C_Detection_L.clear()
        self.ui.Front_After_C_Detection_L.clear()
        self.ui.Back_After_C_Detection_L.clear()
        self.ui.Matrix_Image_L.clear()    
        self.ui.PPID_Recogniton_L.setText(f'PPID: ')
        self.ui.PPID_LE.clear()
        self.ui.Saved_PPID_L.setText(f'Saved PPID: ')
        self.ui.PPID_Result_L.setText(f'Saved PPID: ')
            
class ImageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_ImageWindow()
        self.ui.setupUi(self)
        
        ### Button Connections
        ## Current List That Holds The Paths To Images That Can Be Viewed
        self.Image_Paths = []
        self.CurrentPath = 0
        
        ## Window Flags
        # Removes Default Window Flags
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Custom Window Flag Connections
        self.ui.Close_B.clicked.connect(lambda: self.close())
        self.ui.Maximize_B.clicked.connect(lambda: self.Restore_Or_Maximize_Window())
        self.ui.Minimize_B.clicked.connect(lambda: self.showMinimized())

        # Shortcut Connections
        self.ui.ESC_Shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("ESC"), self)
        self.ui.ESC_Shortcut.activated.connect(lambda: self.close())
        self.ui.Left_Shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Left"), self)
        self.ui.Left_Shortcut.activated.connect(lambda: self.Previous_Image())
        self.ui.Right_Shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Right"), self)
        self.ui.Right_Shortcut.activated.connect(lambda: self.Next_Image())

        # Custom Window Size Grip Connection
        QtWidgets.QSizeGrip(self.ui.Window_Size_Grip)
        
        ## Move Window By Dragging Window Header Connection
        self.ui.Header_Container.mouseMoveEvent = self.Move_Window
        self.ui.Header_Container.mousePressEvent = self.Mouse_Press

        ## Change Pages Using Footer Button Connections
        # Go To Previous Page
        self.ui.Previous_Image_B.clicked.connect(lambda: self.Previous_Image())
        # Go To Next Page
        self.ui.Next_Image_B.clicked.connect(lambda: self.Next_Image())

    ## Maximize And Minimize Window Function
    def Restore_Or_Maximize_Window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.Maximize_B.setIcon(QtGui.QIcon(u":/Icons/Icons2/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.Maximize_B.setIcon(QtGui.QIcon(u":/Icons/Icons2/minimize-2.svg"))
    
    ## Click And Drag Window Using Header Functions
    # Register Click ON The Header
    def Mouse_Press(self, event):
        self.dragPos = self.pos()
        self.mouse_original_pos = self.mapToGlobal(event.pos())
            
    # Move The Window 
    def Move_Window(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                MainWindow_last_pos = self.dragPos + self.mapToGlobal(event.pos()) - self.mouse_original_pos
                self.move(MainWindow_last_pos)
                event.accept()


    ## Get List of Image Paths
    def Get_Image_Paths(self, paths):
        self.Image_Paths = paths
        self.ui.Image_L.setPixmap(QtGui.QPixmap(self.Image_Paths[0]))
        self.CurrentPath = 0

    ## Change Page Using Footer Buttons Functions
    # View Previous Page
    def Previous_Image(self):
        if self.CurrentPath == 0:
            self.ui.Image_L.setPixmap(QtGui.QPixmap(self.Image_Paths[len(self.Image_Paths) - 1]))
            self.CurrentPath = len(self.Image_Paths) - 1
        else:
            self.ui.Image_L.setPixmap(QtGui.QPixmap(self.Image_Paths[self.CurrentPath - 1]))
            self.CurrentPath -= 1

    # View Next Page
    def Next_Image(self):
        if self.CurrentPath == (len(self.Image_Paths) - 1):
            self.ui.Image_L.setPixmap(QtGui.QPixmap(self.Image_Paths[0]))
            self.CurrentPath = 0
        else:
            self.ui.Image_L.setPixmap(QtGui.QPixmap(self.Image_Paths[self.CurrentPath + 1]))
            self.CurrentPath += 1

## Class For Image Capture Thread
class ImageCapture(QtCore.QThread):
    ImageUpdate = QtCore.pyqtSignal(QtGui.QImage)
    UpdateCapturedFront = QtCore.pyqtSignal(QtGui.QImage)
    UpdateCapturedBack = QtCore.pyqtSignal(QtGui.QImage)
    CaptureFront = False
    CaptureBack = False

    def run(self):
        # Video Capture Initialization
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Connect to camera
        Capture.set(cv2.CAP_PROP_FRAME_WIDTH, 8000)
        Capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 6000)

        # Image Label Scaling Calculations
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        Scaled_Width = int(screen_width / 2.5)
        Scaled_Height = int(screen_height / 2.8)

        while self.ThreadActive:
            ret, frame = Capture.read()  # Capture a frame

            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, -1)
                ConvertToQtFormat = QtGui.QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QtGui.QImage.Format_RGB888)
                Picture = ConvertToQtFormat.scaled(Scaled_Width, Scaled_Height, QtCore.Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Picture)

                if self.CaptureFront:
                    os.chdir(Paths.Captured_Images_Path)
                    cv2.imwrite("Front.png", cv2.flip(frame, -1))
                    os.chdir(Paths.Home_Path)
                    FrontImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedFrontImage = cv2.flip(FrontImage, -1)
                    FrontImageConvertToQtFormat = QtGui.QImage(FlippedFrontImage.data, FlippedFrontImage.shape[1], FlippedFrontImage.shape[0], QtGui.QImage.Format_RGB888)
                    FrontPicture = FrontImageConvertToQtFormat.scaled(Scaled_Width, Scaled_Height, QtCore.Qt.KeepAspectRatio)
                    self.UpdateCapturedFront.emit(FrontPicture)
                    self.CaptureFront = False

                if self.CaptureBack:
                    os.chdir(Paths.Captured_Images_Path)
                    cv2.imwrite("Back.png", cv2.flip(frame, -1))
                    os.chdir(Paths.Home_Path)
                    BackImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedBackImage = cv2.flip(BackImage, -1)
                    BackImageConvertToQtFormat = QtGui.QImage(FlippedBackImage.data, FlippedBackImage.shape[1], FlippedBackImage.shape[0], QtGui.QImage.Format_RGB888)
                    BackPicture = BackImageConvertToQtFormat.scaled(Scaled_Width, Scaled_Height, QtCore.Qt.KeepAspectRatio)
                    self.UpdateCapturedBack.emit(BackPicture)
                    self.CaptureBack = False

        Capture.release()

    def Stop(self):
        self.ThreadActive = False
        self.quit()

    def Capture_Front(self):
        self.CaptureFront = True

    def Capture_Back(self):
        self.CaptureBack = True
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    image_window = ImageWindow()
    main_window.show()
    sys.exit(app.exec_())
