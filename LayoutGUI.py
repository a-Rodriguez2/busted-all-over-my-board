# Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import Icons_rc
import tkinter as tk

"""
Object Hierarchy

1: MainWindow
    2: centralwidget

        3: Main_Body_Container

            4: Footer_Container
                5: Next_Page_F
                    6: Next_Page_B
                5: Previous_Page_F
                    6: Previous_Page_B
                5: Size_Grip

            4: Header_Container
                5: Open_Slide_F
                    6: Open_Slide_B
                5: Window_Options_F
                    6: Close_B
                    6: Maximize_B
                    6: Minimize_B

            4: Main_Body_Content
                5: stackedWidget

                    6: page_1_1
                        7: Identification_F
                            8: Identification_Title_L
                            8: Station_Number_F
                                9: Station_Number_LE
                                9: Station_Number_Save_B
                                9: Station_Number_Title_L
                            8: View_Entered_Station_Number_F
                                9: Saved_Station_Number_L
                            8: View_Entered_Work_ID_F
                                9: Saved_Work_ID_L
                            8: Work_ID_F
                                9: Work_ID_LE
                                9: Work_ID_Save_B
                                9: Work_ID_Title_L

                    6: page_2_1
                        7: Images_Captured_F
                            8: Back_Image_F
                                9: Back_Image_L
                            8: Captured_Back_Image_Title_L
                            8: Captured_Front_Image_Title_L
                            8: Front_Image_F
                                9: Front_Image_L
                        7: Live_Video_Capture_F
                            8: Capture_Buttons_F
                                9: Capture_Back_B
                                9: Capture_Front_B
                                9: View_Back_B
                                9: View_Front_B
                            8: Capture_Options_Title_L
                            8: Live_Video_F
                                9: Live_Video_L
                            8: Webcam_Live_Feed_Title_L

                    6: page_3_1
                        7: N_Detection_Images_F
                            8: Back_After_N_Detection_F
                                9: Back_After_N_Detection_L
                            8: Back_Before_N_Detection_F
                                9: Back_Before_N_Detection_L
                            8: Front_After_N_Detection_F
                                9: Front_After_N_Detection_L
                            8: Front_Before_N_Detection_F
                                9: Front_Before_N_Detection_L
                        7: N_Detection_Otions_F
                            8: Detect_2D_Data_Matrix_B
                            8: Detect_All_B
                            8: Detect_Defects_B
                            8: Detect_ID_Block_B
                            8: Detect_IOPorts_CardSlots_B
                            8: See_N_Detected_Images_B

                    6: page_3_2
                        7: C_Detection_Images_F
                            8: Back_After_C_Detection_F
                                9: Back_After_C_Detection_L
                            8: Back_Before_C_Detection_F
                                9: Back_Before_C_Detection_L
                            8: Front_After_C_Detection_F
                                9: Front_After_C_Detection_L
                            8: Front_Before_C_Detection_F
                                9: Front_Before_C_Detection_L
                        7: N_Detection_Otions_F
                            8: C_Detection_Buttons_F
                                9: Check_All_B
                                9: Run_C_Detection_B
                                9: Uncheck_All_B
                                9: View_After_C_Detection_B
                                9: View_Before_C_Detection_B
                            8: C_Detection_Check_Boxes_F
                                9: A_2D_Data_Matrix_CB
                                9: Audio_CB
                                9: Battery_CB
                                9: Bent_Pins_CB
                                9: Burn_CB
                                9: Card_Slot_SSD_CB
                                9: Card_Slot_WLAN_CB
                                9: Card_Slot_WWAN_CB
                                9: Discoloration_CB
                                9: Ethernet_CB
                                9: Fan_CB
                                9: HDMI_CB
                                9: ID_Block_CB
                                9: Micro_SD_CB
                                9: Micro_SIM_CB
                                9: Missing_CB
                                9: RAM_CB
                                9: Speaker_CB
                                9: Thermal_Paste_CB
                                9: USB_CB

                    6: page_3_3
                        7: Manual_Identification_F
                            8: Manual_Identification_Title_L
                            8: Manual_PN_F
                                9: PN_LE
                                9: PN_Save_B
                                9: PN_Title_L
                            8: Manual_PPID_F
                                9: PPID_LE
                                9: PPID_Save_B
                                9: PPID_Title_L
                            8: View_Manual_Entered_PN_F
                                9: Saved_PN_L
                            8: View_Manual_Entered_PPID_F
                                9: Saved_PPID_L
                        7: Matrix_F
                            8: Matrix_Image_F
                                9: Matrix_Image_L
                            8: Matrix_Results_F
                                9: Matrix_Results_Title_L
                                9: PN_Recogniton_L
                                9: PPID_Recogniton_L
                                9: Run_Recognition_B
                                9: Save_Results_B

                    6: page_4_1
                        7: Results_F
                            8: PN_Result_L
                            8: PPID_Result_L
                            8: Results_Title_L
                            8: Station_Number_Result_L
                            8: Work_ID_Result_L
                        7: Test_And_Report_F
                            8: Report_F
                                9: Generate_Report_B
                                9: Run_Test_File_B
                                9: View_Report_B
                            8: Test_And_Report_Title_L
                            8: Test_F
                                9: Choose_Test_File_B
                                9: Test_File_Name_L
                                9: Test_File_Name_Title_L

        3: Slide_Menu_Container
            4: Slide_Menu

                5: App_Name_F
                    6: App_Name_L

                5: Exit_F
                    6: Exit_B

                5: Options_F
                    6: toolBox

                        7: Home_P
                            8: Home_F
                                9: Home_1A

                        7: Image_Capture_P
                            8: Image_Capture_F
                                9: Image_Capture_Take_1B

                        7: Detection_P
                            8: Detection_F
                                9: Detection_Custom_2B
                                9: Detection_Matrix_3B
                                9: Detection_Normal_1B

                        7: Testing_P
                            8: Testing_F
                                9: Testing_1B
"""

## Main GUI Window Class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 1: Main Window Properties
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1387, 911)
        MainWindow.setStyleSheet("*{\n"
        "    border: none;\n"
        "    color: rgb(167, 167, 167);\n"
        "}")

        ## 2: Central Widget Properties
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(45, 45, 48);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #-----------------------------------------------------------------------------------------------------------------------------------------#

        ### 3: Slide Menu Container Frame
        self.Slide_Menu_Container = QtWidgets.QFrame(self.centralwidget)
        self.Slide_Menu_Container.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slide_Menu_Container.sizePolicy().hasHeightForWidth())
        self.Slide_Menu_Container.setSizePolicy(sizePolicy)
        self.Slide_Menu_Container.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Slide_Menu_Container.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Slide_Menu_Container.setObjectName("Slide_Menu_Container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Slide_Menu_Container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #### 4: Slide Menu Frame
        self.Slide_Menu = QtWidgets.QFrame(self.Slide_Menu_Container)
        self.Slide_Menu.setMinimumSize(QtCore.QSize(198, 0))
        self.Slide_Menu.setObjectName("Slide_Menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Slide_Menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        ##### 5: Slide Menu App Name Label Frame
        self.App_Name_F = QtWidgets.QFrame(self.Slide_Menu)
        self.App_Name_F.setObjectName("App_Name_F")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.App_Name_F)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        ###### 6: Slide Menu App Name Label
        self.App_Name_L = QtWidgets.QLabel(self.App_Name_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.App_Name_L.setFont(font)
        self.App_Name_L.setStyleSheet("")
        self.App_Name_L.setAlignment(QtCore.Qt.AlignCenter)
        self.App_Name_L.setWordWrap(True)
        self.App_Name_L.setObjectName("App_Name_L")
        self.horizontalLayout_6.addWidget(self.App_Name_L)
        self.verticalLayout_5.addWidget(self.App_Name_F, 0, QtCore.Qt.AlignTop)
        ##### 5: Slide Menu Options Frame
        self.Options_F = QtWidgets.QFrame(self.Slide_Menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Options_F.sizePolicy().hasHeightForWidth())
        self.Options_F.setSizePolicy(sizePolicy)
        self.Options_F.setObjectName("Options_F")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Options_F)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        ###### 6: Slide Menu Options Toolbox Frame
        self.toolBox = QtWidgets.QToolBox(self.Options_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("QToolBox{\n"
        "    background-color: rgb(45, 45, 48);\n"
        "    text-align:left;\n"
        "    icon-size: 20px\n"
        "}\n"
        "QToolBox::tab{\n"
        "    border-radius: 5px;\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    text-align:left;\n"
        "}\n"
        "\n"
        "QToolBox::tab:selected{\n"
        "    color: rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QToolBox::tab:hover{\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QToolBox::tab:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "")
        self.toolBox.setObjectName("toolBox")
        ####### 7: Home Tab Widget
        self.Home_P = QtWidgets.QWidget()
        self.Home_P.setGeometry(QtCore.QRect(0, 0, 250, 671))
        self.Home_P.setObjectName("Home_P")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Home_P)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        ######## 8: Home Tab Frame
        self.Home_F = QtWidgets.QFrame(self.Home_P)
        self.Home_F.setObjectName("Home_F")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Home_F)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        ######### 9: Home Tab Button 1
        self.Home_1A = QtWidgets.QPushButton(self.Home_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Home_1A.setFont(font)
        self.Home_1A.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}")
        ########## 10: Identification Tab Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons2/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_1A.setIcon(icon)
        self.Home_1A.setIconSize(QtCore.QSize(24, 24))
        self.Home_1A.setObjectName("Home_1A")
        self.verticalLayout_12.addWidget(self.Home_1A)
        self.verticalLayout_7.addWidget(self.Home_F, 0, QtCore.Qt.AlignTop)
        ########### 11: Home Tab Icon
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons2/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.Home_P, icon1, "")
        ####### 7: Image Capture Tab Widget
        self.Image_Capture_P = QtWidgets.QWidget()
        self.Image_Capture_P.setGeometry(QtCore.QRect(0, 0, 198, 744))
        self.Image_Capture_P.setObjectName("Image_Capture_P")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Image_Capture_P)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        ######## 8: Image Capture Tab Frame
        self.Image_Capture_F = QtWidgets.QFrame(self.Image_Capture_P)
        self.Image_Capture_F.setObjectName("Image_Capture_F")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Image_Capture_F)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        ######### 9: Image Capture Tab Button 1
        self.Image_Capture_Take_1B = QtWidgets.QPushButton(self.Image_Capture_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Image_Capture_Take_1B.setFont(font)
        self.Image_Capture_Take_1B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}")
        ########## 10: Take Pictures Tab Icon
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons2/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Image_Capture_Take_1B.setIcon(icon2)
        self.Image_Capture_Take_1B.setIconSize(QtCore.QSize(24, 24))
        self.Image_Capture_Take_1B.setObjectName("Image_Capture_Take_1B")
        self.verticalLayout_13.addWidget(self.Image_Capture_Take_1B)
        self.verticalLayout_8.addWidget(self.Image_Capture_F, 0, QtCore.Qt.AlignTop)
        ########### 11: Image Capture Tab Icon
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons2/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.Image_Capture_P, icon3, "")
        ####### 7: Detection Tab Widget
        self.Detection_P = QtWidgets.QWidget()
        self.Detection_P.setGeometry(QtCore.QRect(0, 0, 250, 671))
        self.Detection_P.setObjectName("Detection_P")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Detection_P)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        ######## 8: Detection Tab Frame
        self.Detection_F = QtWidgets.QFrame(self.Detection_P)
        self.Detection_F.setObjectName("Detection_F")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Detection_F)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        ######### 9: Detection Tab Button 1
        self.Detection_Normal_1B = QtWidgets.QPushButton(self.Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Detection_Normal_1B.setFont(font)
        self.Detection_Normal_1B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}")
        ########## 10: Custom Detection Tab Icon
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons2/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Detection_Normal_1B.setIcon(icon4)
        self.Detection_Normal_1B.setIconSize(QtCore.QSize(32, 24))
        self.Detection_Normal_1B.setObjectName("Detection_Normal_1B")
        self.verticalLayout_14.addWidget(self.Detection_Normal_1B)
        ######### 9: Detection Tab Button 2
        self.Detection_Custom_2B = QtWidgets.QPushButton(self.Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Detection_Custom_2B.setFont(font)
        self.Detection_Custom_2B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}")
        ########## 10: Custom Detection Tab Icon
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/Icons2/sliders.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Detection_Custom_2B.setIcon(icon5)
        self.Detection_Custom_2B.setIconSize(QtCore.QSize(24, 24))
        self.Detection_Custom_2B.setObjectName("Detection_Custom_2B")
        self.verticalLayout_14.addWidget(self.Detection_Custom_2B)
        ######### 9: Detection Tab Button 3
        self.Detection_Matrix_3B = QtWidgets.QPushButton(self.Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Detection_Matrix_3B.setFont(font)
        self.Detection_Matrix_3B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}")
        ########## 10: 2D Data Matrix Tab Icon
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/Icons2/grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Detection_Matrix_3B.setIcon(icon6)
        self.Detection_Matrix_3B.setIconSize(QtCore.QSize(24, 24))
        self.Detection_Matrix_3B.setObjectName("Detection_Matrix_3B")
        self.verticalLayout_14.addWidget(self.Detection_Matrix_3B)
        self.verticalLayout_9.addWidget(self.Detection_F, 0, QtCore.Qt.AlignTop)
        ########### 11: Detection Tab Icon
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/Icons2/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.Detection_P, icon7, "")
        ####### 7: Testing Tab Widget
        self.Testing_P = QtWidgets.QWidget()
        self.Testing_P.setGeometry(QtCore.QRect(0, 0, 250, 671))
        self.Testing_P.setObjectName("Testing_P")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Testing_P)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        ######## 8: Testing Tab Frame
        self.Testing_F = QtWidgets.QFrame(self.Testing_P)
        self.Testing_F.setObjectName("Testing_F")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.Testing_F)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        ######### 9: Testing Tab Button 1
        self.Testing_1B = QtWidgets.QPushButton(self.Testing_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Testing_1B.setFont(font)
        self.Testing_1B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 5px;\n"
        "}")
        ########## 10: Generate Report Tab Icon
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/Icons2/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Testing_1B.setIcon(icon8)
        self.Testing_1B.setIconSize(QtCore.QSize(24, 24))
        self.Testing_1B.setObjectName("Testing_1B")
        self.verticalLayout_15.addWidget(self.Testing_1B)
        self.verticalLayout_10.addWidget(self.Testing_F, 0, QtCore.Qt.AlignTop)
        ########### 11: Testing Tab Icon
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/Icons2/zap.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.Testing_P, icon9, "")
        self.verticalLayout_6.addWidget(self.toolBox)
        self.verticalLayout_5.addWidget(self.Options_F)
        
        ##### 5: Slide Menu Exit Button Frame
        self.Exit_F = QtWidgets.QFrame(self.Slide_Menu)
        self.Exit_F.setStyleSheet("")
        self.Exit_F.setObjectName("Exit_F")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Exit_F)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        ###### 6: Slide Menu Exit Frame
        self.Exit_B = QtWidgets.QPushButton(self.Exit_F)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Exit_B.setFont(font)
        self.Exit_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}\n"
        "")
        ####### 7: Slide Menu Exit Icon
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icons/Icons2/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_B.setIcon(icon10)
        self.Exit_B.setIconSize(QtCore.QSize(32, 24))
        self.Exit_B.setObjectName("Exit_B")
        self.horizontalLayout_7.addWidget(self.Exit_B, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.Exit_F)
        self.verticalLayout_2.addWidget(self.Slide_Menu)
        self.horizontalLayout.addWidget(self.Slide_Menu_Container)
        #-----------------------------------------------------------------------------------------------------------------------------------------#
        
        ### 3: Main Body Container Frame
        self.Main_Body_Container = QtWidgets.QFrame(self.centralwidget)
        self.Main_Body_Container.setObjectName("Main_Body_Container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Main_Body_Container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        #### 4: Header Container Frame
        self.Header_Container = QtWidgets.QFrame(self.Main_Body_Container)
        self.Header_Container.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Header_Container.setObjectName("Header_Container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header_Container)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        ##### 5: Open Slide Button Frame
        self.Open_Slide_F = QtWidgets.QFrame(self.Header_Container)
        self.Open_Slide_F.setObjectName("Open_Slide_F")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Open_Slide_F)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        ###### 6: Open Slide Button
        self.Open_Slide_B = QtWidgets.QPushButton(self.Open_Slide_F)
        self.Open_Slide_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}\n"
        "")
        self.Open_Slide_B.setText("")
        ####### 7: Open Slide Icon
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icons/Icons2/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Open_Slide_B.setIcon(icon11)
        self.Open_Slide_B.setIconSize(QtCore.QSize(32, 32))
        self.Open_Slide_B.setObjectName("Open_Slide_B")
        self.horizontalLayout_5.addWidget(self.Open_Slide_B)
        self.horizontalLayout_2.addWidget(self.Open_Slide_F, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        ##### 5: Window Options Frame
        self.Window_Options_F = QtWidgets.QFrame(self.Header_Container)
        self.Window_Options_F.setObjectName("Window_Options_F")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Window_Options_F)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        ###### 6: Minimize Button
        self.Minimize_B = QtWidgets.QPushButton(self.Window_Options_F)
        self.Minimize_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}\n"
        "")
        self.Minimize_B.setText("")
        ####### 7: Minimize Icon 
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icons/Icons2/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimize_B.setIcon(icon12)
        self.Minimize_B.setIconSize(QtCore.QSize(32, 32))
        self.Minimize_B.setObjectName("Minimize_B")
        self.horizontalLayout_4.addWidget(self.Minimize_B)
        ###### 6: Maximize Button
        self.Maximize_B = QtWidgets.QPushButton(self.Window_Options_F)
        self.Maximize_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Maximize_B.setText("")
        ####### 7: Maximize Icon 
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Icons/Icons2/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Maximize_B.setIcon(icon13)
        self.Maximize_B.setIconSize(QtCore.QSize(32, 32))
        self.Maximize_B.setObjectName("Maximize_B")
        self.horizontalLayout_4.addWidget(self.Maximize_B)
        ###### 6: Close Button
        self.Close_B = QtWidgets.QPushButton(self.Window_Options_F)
        self.Close_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Close_B.setText("")
        ####### 7: Close Icon 
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Icons/Icons2/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_B.setIcon(icon14)
        self.Close_B.setIconSize(QtCore.QSize(32, 32))
        self.Close_B.setObjectName("Close_B")
        self.horizontalLayout_4.addWidget(self.Close_B)
        self.horizontalLayout_2.addWidget(self.Window_Options_F, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Header_Container)
        
        #### 4: Main Body Content Container Frame
        self.Main_Body_Content = QtWidgets.QFrame(self.Main_Body_Container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Body_Content.sizePolicy().hasHeightForWidth())
        self.Main_Body_Content.setSizePolicy(sizePolicy)
        self.Main_Body_Content.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0, 122, 204)\n"
        "}")
        self.Main_Body_Content.setObjectName("Main_Body_Content")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Main_Body_Content)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        ##### 5: Main Window Stacked Widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.Main_Body_Content)
        self.stackedWidget.setObjectName("stackedWidget")
        ###### 6: Tab 1 Page 1 Stacked Widget ( Identification Page )
        self.page_1_1 = QtWidgets.QWidget()
        self.page_1_1.setObjectName("page_1_1")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_1_1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        ####### 7: Identification Page Frame
        self.Identification_F = QtWidgets.QFrame(self.page_1_1)
        self.Identification_F.setObjectName("Identification_F")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.Identification_F)
        self.verticalLayout_57.setContentsMargins(64, 1, 64, 1)
        self.verticalLayout_57.setSpacing(16)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.Identification_Title_L = QtWidgets.QLabel(self.Identification_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Identification_Title_L.sizePolicy().hasHeightForWidth())
        self.Identification_Title_L.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        ######## 8: Identification Title Label
        self.Identification_Title_L.setFont(font)
        self.Identification_Title_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Identification_Title_L.setObjectName("Identification_Title_L")
        self.verticalLayout_57.addWidget(self.Identification_Title_L)
        self.Station_Number_F = QtWidgets.QFrame(self.Identification_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station_Number_F.sizePolicy().hasHeightForWidth())
        ######## 8: Station Number Frame
        self.Station_Number_F.setSizePolicy(sizePolicy)
        self.Station_Number_F.setObjectName("Station_Number_F")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Station_Number_F)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        ######### 9: Station Number Title Label
        self.Station_Number_Title_L = QtWidgets.QLabel(self.Station_Number_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Station_Number_Title_L.setFont(font)
        self.Station_Number_Title_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 10px")
        self.Station_Number_Title_L.setObjectName("Station_Number_Title_L")
        self.horizontalLayout_10.addWidget(self.Station_Number_Title_L)
        ######### 9: Station Number Line Edit
        self.Station_Number_LE = QtWidgets.QLineEdit(self.Station_Number_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station_Number_LE.sizePolicy().hasHeightForWidth())
        self.Station_Number_LE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Station_Number_LE.setFont(font)
        self.Station_Number_LE.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(30, 30, 30);\n"
        "    border-radius: 10px;\n"
        "    padding: 10px;\n"
        "}\n"
        "\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}")
        self.Station_Number_LE.setObjectName("Station_Number_LE")
        self.horizontalLayout_10.addWidget(self.Station_Number_LE)
        ######### 9: Save Station Number Button
        self.Station_Number_Save_B = QtWidgets.QPushButton(self.Station_Number_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Station_Number_Save_B.setFont(font)
        self.Station_Number_Save_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Station_Number_Save_B.setObjectName("Station_Number_Save_B")
        self.horizontalLayout_10.addWidget(self.Station_Number_Save_B)
        self.verticalLayout_57.addWidget(self.Station_Number_F)
        ######## 8: View Entered Station Number Frame
        self.View_Entered_Station_Number_F = QtWidgets.QFrame(self.Identification_F)
        self.View_Entered_Station_Number_F.setObjectName("View_Entered_Station_Number_F")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.View_Entered_Station_Number_F)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        ######### 9: Saved Station Number Label
        self.Saved_Station_Number_L = QtWidgets.QLabel(self.View_Entered_Station_Number_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Saved_Station_Number_L.setFont(font)
        self.Saved_Station_Number_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px;")
        self.Saved_Station_Number_L.setObjectName("Saved_Station_Number_L")
        self.horizontalLayout_28.addWidget(self.Saved_Station_Number_L)
        self.verticalLayout_57.addWidget(self.View_Entered_Station_Number_F)
        ######## 8: Work ID Frame
        self.Work_ID_F = QtWidgets.QFrame(self.Identification_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Work_ID_F.sizePolicy().hasHeightForWidth())
        self.Work_ID_F.setSizePolicy(sizePolicy)
        self.Work_ID_F.setObjectName("Work_ID_F")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.Work_ID_F)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        ######### 9: Work ID Title Label
        self.Work_ID_Title_L = QtWidgets.QLabel(self.Work_ID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Work_ID_Title_L.setFont(font)
        self.Work_ID_Title_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 10px")
        self.Work_ID_Title_L.setObjectName("Work_ID_Title_L")
        self.horizontalLayout_16.addWidget(self.Work_ID_Title_L)
        ######### 9: Work ID Line Edit
        self.Work_ID_LE = QtWidgets.QLineEdit(self.Work_ID_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Work_ID_LE.sizePolicy().hasHeightForWidth())
        self.Work_ID_LE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Work_ID_LE.setFont(font)
        self.Work_ID_LE.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Work_ID_LE.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(30, 30, 30);\n"
        "    border-radius: 10px;\n"
        "    padding: 10px;\n"
        "}\n"
        "\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}")
        self.Work_ID_LE.setObjectName("Work_ID_LE")
        self.horizontalLayout_16.addWidget(self.Work_ID_LE)
        ######### 9: Save Work ID Button
        self.Work_ID_Save_B = QtWidgets.QPushButton(self.Work_ID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Work_ID_Save_B.setFont(font)
        self.Work_ID_Save_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Work_ID_Save_B.setObjectName("Work_ID_Save_B")
        self.horizontalLayout_16.addWidget(self.Work_ID_Save_B)
        self.verticalLayout_57.addWidget(self.Work_ID_F)
        ######## 8: View Entered Work ID Frame
        self.View_Entered_Work_ID_F = QtWidgets.QFrame(self.Identification_F)
        self.View_Entered_Work_ID_F.setStyleSheet("")
        self.View_Entered_Work_ID_F.setObjectName("View_Entered_Work_ID_F")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.View_Entered_Work_ID_F)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        ######### 9: Saved Work ID Label
        self.Saved_Work_ID_L = QtWidgets.QLabel(self.View_Entered_Work_ID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Saved_Work_ID_L.setFont(font)
        self.Saved_Work_ID_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px;")
        self.Saved_Work_ID_L.setObjectName("Saved_Work_ID_L")
        self.horizontalLayout_26.addWidget(self.Saved_Work_ID_L)
        self.verticalLayout_57.addWidget(self.View_Entered_Work_ID_F)
        self.verticalLayout_16.addWidget(self.Identification_F, 0, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_1_1)
        ###### 6: Tab 2 Page 1 Stacked Widget ( Take Pictures Page )
        self.page_2_1 = QtWidgets.QWidget()
        self.page_2_1.setObjectName("page_2_1")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_2_1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        ####### 7: Live Video Capture Frame
        self.Live_Video_Capture_F = QtWidgets.QFrame(self.page_2_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Live_Video_Capture_F.sizePolicy().hasHeightForWidth())
        self.Live_Video_Capture_F.setSizePolicy(sizePolicy)
        self.Live_Video_Capture_F.setStyleSheet("")
        self.Live_Video_Capture_F.setObjectName("Live_Video_Capture_F")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Live_Video_Capture_F)
        self.gridLayout_7.setContentsMargins(64, 1, 64, -1)
        self.gridLayout_7.setHorizontalSpacing(64)
        self.gridLayout_7.setObjectName("gridLayout_7")
        ######## 8: Live Video Title Label
        self.Webcam_Live_Feed_Title_L = QtWidgets.QLabel(self.Live_Video_Capture_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Webcam_Live_Feed_Title_L.setFont(font)
        self.Webcam_Live_Feed_Title_L.setStyleSheet("padding: 5px;")
        self.Webcam_Live_Feed_Title_L.setFrameShape(QtWidgets.QFrame.VLine)
        self.Webcam_Live_Feed_Title_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Webcam_Live_Feed_Title_L.setObjectName("Webcam_Live_Feed_Title_L")
        self.gridLayout_7.addWidget(self.Webcam_Live_Feed_Title_L, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        ######## 8: Capture Options Title Label
        self.Capture_Options_L = QtWidgets.QLabel(self.Live_Video_Capture_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Capture_Options_L.setFont(font)
        self.Capture_Options_L.setStyleSheet("padding: 5px;")
        self.Capture_Options_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Capture_Options_L.setObjectName("Capture_Options_L")
        self.gridLayout_7.addWidget(self.Capture_Options_L, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        ######### 8: Live Video Frame
        self.Live_Video_F = QtWidgets.QFrame(self.Live_Video_Capture_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Live_Video_F.sizePolicy().hasHeightForWidth())
        self.Live_Video_F.setSizePolicy(sizePolicy)
        self.Live_Video_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Live_Video_F.setObjectName("Live_Video_F")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.Live_Video_F)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.gridLayout_7.addWidget(self.Live_Video_F, 3, 0, 1, 1)
        ######### 9: Live Video Label
        self.Live_Video_L = QtWidgets.QLabel(self.Live_Video_F)
        self.Live_Video_L.setEnabled(True)
        self.Live_Video_L.setText("")
        self.Live_Video_L.setPixmap(QtGui.QPixmap())
        self.Live_Video_L.setScaledContents(True)
        self.Live_Video_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Live_Video_L.setObjectName("Live_Video_L")
        self.verticalLayout_39.addWidget(self.Live_Video_L)
        self.gridLayout_7.addWidget(self.Live_Video_F, 1, 0, 1, 1)
        ######## 8: Capture Buttons Frame
        self.Capture_Buttons_F = QtWidgets.QFrame(self.Live_Video_Capture_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Capture_Buttons_F.sizePolicy().hasHeightForWidth())
        self.Capture_Buttons_F.setSizePolicy(sizePolicy)
        self.Capture_Buttons_F.setObjectName("Capture_Buttons_F")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Capture_Buttons_F)
        self.gridLayout_5.setSpacing(32)
        self.gridLayout_5.setObjectName("gridLayout_5")
        ######### 9: View Captured Front Image Button
        self.View_Front_B = QtWidgets.QPushButton(self.Capture_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.View_Front_B.setFont(font)
        self.View_Front_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.View_Front_B.setObjectName("View_Front_B")
        self.gridLayout_5.addWidget(self.View_Front_B, 0, 1, 1, 1)
        ######### 9: Capture Back Image Button
        self.Capture_Front_B = QtWidgets.QPushButton(self.Capture_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Capture_Front_B.setFont(font)
        self.Capture_Front_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Capture_Front_B.setObjectName("Capture_Front_B")
        self.gridLayout_5.addWidget(self.Capture_Front_B, 0, 0, 1, 1)
        ######### 9: View Captured Back Image Button
        self.View_Back_B = QtWidgets.QPushButton(self.Capture_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.View_Back_B.setFont(font)
        self.View_Back_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.View_Back_B.setObjectName("View_Back_B")
        self.gridLayout_5.addWidget(self.View_Back_B, 1, 1, 1, 1)
        ######### 9: Capture Back Image Button
        self.Capture_Back_B = QtWidgets.QPushButton(self.Capture_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Capture_Back_B.setFont(font)
        self.Capture_Back_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Capture_Back_B.setObjectName("Capture_Back_B")
        self.gridLayout_5.addWidget(self.Capture_Back_B, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.Capture_Buttons_F, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_17.addWidget(self.Live_Video_Capture_F)
        ####### 7: Images Captured Frame
        self.Images_Captured_F = QtWidgets.QFrame(self.page_2_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Images_Captured_F.sizePolicy().hasHeightForWidth())
        self.Images_Captured_F.setSizePolicy(sizePolicy)
        self.Images_Captured_F.setObjectName("Images_Captured_F")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Images_Captured_F)
        self.gridLayout_6.setContentsMargins(64, -1, 64, 1)
        self.gridLayout_6.setHorizontalSpacing(64)
        self.gridLayout_6.setObjectName("gridLayout_6")
        ######## 8: Captured Back Image Frame
        self.Back_Image_F = QtWidgets.QFrame(self.Images_Captured_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back_Image_F.sizePolicy().hasHeightForWidth())
        self.Back_Image_F.setSizePolicy(sizePolicy)
        self.Back_Image_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Back_Image_F.setObjectName("Back_Image_F")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.Back_Image_F)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        ######### 9: Captured Back Image Label
        self.Back_Image_L = QtWidgets.QLabel(self.Back_Image_F)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.Back_Image_L.setFont(font)
        self.Back_Image_L.setText("")
        self.Back_Image_L.setPixmap(QtGui.QPixmap())
        self.Back_Image_L.setScaledContents(True)
        self.Back_Image_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_Image_L.setObjectName("Back_Image_L")
        self.verticalLayout_19.addWidget(self.Back_Image_L)
        self.gridLayout_6.addWidget(self.Back_Image_F, 1, 1, 1, 1)
        ######## 8: Captured Front Image Frame
        self.Front_Image_F = QtWidgets.QFrame(self.Images_Captured_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Front_Image_F.sizePolicy().hasHeightForWidth())
        self.Front_Image_F.setSizePolicy(sizePolicy)
        self.Front_Image_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Front_Image_F.setObjectName("Front_Image_F")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Front_Image_F)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        ######### 9: Captured Front Image Label
        self.Front_Image_L = QtWidgets.QLabel(self.Front_Image_F)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.Front_Image_L.setFont(font)
        self.Front_Image_L.setText("")
        self.Front_Image_L.setPixmap(QtGui.QPixmap())
        self.Front_Image_L.setScaledContents(True)
        self.Front_Image_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Front_Image_L.setObjectName("Front_Image_L")
        self.verticalLayout_18.addWidget(self.Front_Image_L)
        self.gridLayout_6.addWidget(self.Front_Image_F, 1, 0, 1, 1)
        ######## 8: Captured Front Image Title Label
        self.Captured_Front_Image_L = QtWidgets.QLabel(self.Images_Captured_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Captured_Front_Image_L.setFont(font)
        self.Captured_Front_Image_L.setStyleSheet("padding: 5px;")
        self.Captured_Front_Image_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Captured_Front_Image_L.setObjectName("Captured_Front_Image_L")
        self.gridLayout_6.addWidget(self.Captured_Front_Image_L, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        ######## 8: Captured Back Image Title Label
        self.Captured_Back_Image_L = QtWidgets.QLabel(self.Images_Captured_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Captured_Back_Image_L.setFont(font)
        self.Captured_Back_Image_L.setStyleSheet("padding: 5px;")
        self.Captured_Back_Image_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Captured_Back_Image_L.setObjectName("Captured_Back_Image_L")
        self.gridLayout_6.addWidget(self.Captured_Back_Image_L, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_17.addWidget(self.Images_Captured_F)
        self.stackedWidget.addWidget(self.page_2_1)
        ###### 6: Tab 3 Page 1 Stacked Widget ( Normal Detection Page )
        self.page_3_1 = QtWidgets.QWidget()
        self.page_3_1.setObjectName("page_3_1")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_3_1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.N_Detection_Images_F = QtWidgets.QFrame(self.page_3_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.N_Detection_Images_F.sizePolicy().hasHeightForWidth())
        ####### 7: Normal Detection Images Frame
        self.N_Detection_Images_F.setSizePolicy(sizePolicy)
        self.N_Detection_Images_F.setObjectName("N_Detection_Images_F")
        self.gridLayout = QtWidgets.QGridLayout(self.N_Detection_Images_F)
        self.gridLayout.setContentsMargins(64, 1, 64, 1)
        self.gridLayout.setHorizontalSpacing(64)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        ######## 8: Front Image Before Normal Detection Frame
        self.Front_Before_N_Detection_F = QtWidgets.QFrame(self.N_Detection_Images_F)
        self.Front_Before_N_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Front_Before_N_Detection_F.setObjectName("Front_Before_N_Detection_F")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.Front_Before_N_Detection_F)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        ######### 9: Front Image Before Normal Detection Label
        self.Front_Before_N_Detection_L = QtWidgets.QLabel(self.Front_Before_N_Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.Front_Before_N_Detection_L.setFont(font)
        self.Front_Before_N_Detection_L.setText("")
        self.Front_Before_N_Detection_L.setPixmap(QtGui.QPixmap())
        self.Front_Before_N_Detection_L.setScaledContents(True)
        self.Front_Before_N_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Front_Before_N_Detection_L.setObjectName("Front_Before_N_Detection_L")
        self.verticalLayout_23.addWidget(self.Front_Before_N_Detection_L)
        self.gridLayout.addWidget(self.Front_Before_N_Detection_F, 0, 0, 1, 1)
        ######## 8: Front Image After Normal Detection Frame
        self.Front_After_N_Detection_F = QtWidgets.QFrame(self.N_Detection_Images_F)
        self.Front_After_N_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Front_After_N_Detection_F.setObjectName("Front_After_N_Detection_F")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.Front_After_N_Detection_F)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        ######### 9: Front Image After Normal Detection Label
        self.Front_After_N_Detection_L = QtWidgets.QLabel(self.Front_After_N_Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.Front_After_N_Detection_L.setFont(font)
        self.Front_After_N_Detection_L.setText("")
        self.Front_After_N_Detection_L.setPixmap(QtGui.QPixmap())
        self.Front_After_N_Detection_L.setScaledContents(True)
        self.Front_After_N_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Front_After_N_Detection_L.setObjectName("Front_After_N_Detection_L")
        self.verticalLayout_24.addWidget(self.Front_After_N_Detection_L)
        self.gridLayout.addWidget(self.Front_After_N_Detection_F, 0, 1, 1, 1)
        ######## 8: Back Image Before Normal Detection Frame
        self.Back_Before_N_Detection_F = QtWidgets.QFrame(self.N_Detection_Images_F)
        self.Back_Before_N_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Back_Before_N_Detection_F.setObjectName("Back_Before_N_Detection_F")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.Back_Before_N_Detection_F)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        ######### 9: Back Image Before Normal Detection Label
        self.Back_Before_N_Detection_L = QtWidgets.QLabel(self.Back_Before_N_Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.Back_Before_N_Detection_L.setFont(font)
        self.Back_Before_N_Detection_L.setText("")
        self.Back_Before_N_Detection_L.setPixmap(QtGui.QPixmap())
        self.Back_Before_N_Detection_L.setScaledContents(True)
        self.Back_Before_N_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_Before_N_Detection_L.setObjectName("Back_Before_N_Detection_L")
        self.verticalLayout_25.addWidget(self.Back_Before_N_Detection_L)
        self.gridLayout.addWidget(self.Back_Before_N_Detection_F, 1, 0, 1, 1)
        ######## 8: Back Image After Normal Detection Frame
        self.Back_After_N_Detection_F = QtWidgets.QFrame(self.N_Detection_Images_F)
        self.Back_After_N_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Back_After_N_Detection_F.setObjectName("Back_After_N_Detection_F")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.Back_After_N_Detection_F)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        ######### 9: Back Image After Normal Detection Label
        self.Back_After_N_Detection_L = QtWidgets.QLabel(self.Back_After_N_Detection_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.Back_After_N_Detection_L.setFont(font)
        self.Back_After_N_Detection_L.setText("")
        self.Back_After_N_Detection_L.setPixmap(QtGui.QPixmap())
        self.Back_After_N_Detection_L.setScaledContents(True)
        self.Back_After_N_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_After_N_Detection_L.setObjectName("Back_After_N_Detection_L")
        self.verticalLayout_26.addWidget(self.Back_After_N_Detection_L)
        self.gridLayout.addWidget(self.Back_After_N_Detection_F, 1, 1, 1, 1)
        self.verticalLayout_22.addWidget(self.N_Detection_Images_F)
        ####### 7: Normal Detection Options Frame
        self.N_Detection_Options_F = QtWidgets.QFrame(self.page_3_1)
        self.N_Detection_Options_F.setObjectName("N_Detection_Options_F")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.N_Detection_Options_F)
        self.gridLayout_4.setContentsMargins(32, -1, 32, 0)
        self.gridLayout_4.setHorizontalSpacing(32)
        self.gridLayout_4.setVerticalSpacing(16)
        self.gridLayout_4.setObjectName("gridLayout_4")
        ######## 8: Detect Defects Button
        self.Detect_Defects_B = QtWidgets.QPushButton(self.N_Detection_Options_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Detect_Defects_B.setFont(font)
        self.Detect_Defects_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Detect_Defects_B.setObjectName("Detect_Defects_B")
        self.gridLayout_4.addWidget(self.Detect_Defects_B, 1, 1, 1, 1)
        ######## 8: Detect 2D Data Matrix Button
        self.Detect_2D_Data_Matrix_B = QtWidgets.QPushButton(self.N_Detection_Options_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Detect_2D_Data_Matrix_B.setFont(font)
        self.Detect_2D_Data_Matrix_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Detect_2D_Data_Matrix_B.setObjectName("Detect_2D_Data_Matrix_B")
        self.gridLayout_4.addWidget(self.Detect_2D_Data_Matrix_B, 0, 4, 1, 1)
        ######## 8: Detect ID Block Button
        self.Detect_ID_Block_B = QtWidgets.QPushButton(self.N_Detection_Options_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Detect_ID_Block_B.setFont(font)
        self.Detect_ID_Block_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Detect_ID_Block_B.setObjectName("Detect_ID_Block_B")
        self.gridLayout_4.addWidget(self.Detect_ID_Block_B, 0, 1, 1, 1)
        ######## 8: Detect All Button
        self.Detect_All_B = QtWidgets.QPushButton(self.N_Detection_Options_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Detect_All_B.setFont(font)
        self.Detect_All_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Detect_All_B.setObjectName("Detect_All_B")
        self.gridLayout_4.addWidget(self.Detect_All_B, 0, 0, 1, 1)
        ######## 8: Detect IO Ports and Card Slots Button
        self.Detect_IOPorts_CardSlots_B = QtWidgets.QPushButton(self.N_Detection_Options_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Detect_IOPorts_CardSlots_B.setFont(font)
        self.Detect_IOPorts_CardSlots_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Detect_IOPorts_CardSlots_B.setObjectName("Detect_IOPorts_CardSlots_B")
        self.gridLayout_4.addWidget(self.Detect_IOPorts_CardSlots_B, 1, 0, 1, 1)
        ######## 8: See All Detected Images Button
        self.See_N_Detected_Images_B = QtWidgets.QPushButton(self.N_Detection_Options_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.See_N_Detected_Images_B.setFont(font)
        self.See_N_Detected_Images_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.See_N_Detected_Images_B.setObjectName("See_N_Detected_Images_B")
        self.gridLayout_4.addWidget(self.See_N_Detected_Images_B, 1, 4, 1, 1)
        self.verticalLayout_22.addWidget(self.N_Detection_Options_F, 0, QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_3_1)
        ###### 6: Tab 3 Page 2 Stacked Widget ( Custom Detection Page )
        self.page_3_2 = QtWidgets.QWidget()
        self.page_3_2.setObjectName("page_3_2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.page_3_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.C_Detection_Images_F = QtWidgets.QFrame(self.page_3_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_Detection_Images_F.sizePolicy().hasHeightForWidth())
        ####### 7: Custom Detection Images Frame
        self.C_Detection_Images_F.setSizePolicy(sizePolicy)
        self.C_Detection_Images_F.setObjectName("C_Detection_Images_F")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.C_Detection_Images_F)
        self.gridLayout_2.setContentsMargins(64, 1, 64, 1)
        self.gridLayout_2.setHorizontalSpacing(64)
        self.gridLayout_2.setVerticalSpacing(16)
        self.gridLayout_2.setObjectName("gridLayout_2")
        ######## 8: Front Image Before Custom Detection Frame
        self.Front_Before_C_Detection_F = QtWidgets.QFrame(self.C_Detection_Images_F)
        self.Front_Before_C_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Front_Before_C_Detection_F.setObjectName("Front_Before_C_Detection_F")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.Front_Before_C_Detection_F)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        ######### 9: Front Image Before Custom Detection Label
        self.Front_Before_C_Detection_L = QtWidgets.QLabel(self.Front_Before_C_Detection_F)
        self.Front_Before_C_Detection_L.setText("")
        self.Front_Before_C_Detection_L.setPixmap(QtGui.QPixmap())
        self.Front_Before_C_Detection_L.setScaledContents(True)
        self.Front_Before_C_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Front_Before_C_Detection_L.setObjectName("Front_Before_C_Detection_L")
        self.verticalLayout_28.addWidget(self.Front_Before_C_Detection_L)
        self.gridLayout_2.addWidget(self.Front_Before_C_Detection_F, 0, 0, 1, 1)
        ######## 8: Front Image After Custom Detection Frame
        self.Front_After_C_Detection_F = QtWidgets.QFrame(self.C_Detection_Images_F)
        self.Front_After_C_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Front_After_C_Detection_F.setObjectName("Front_After_C_Detection_F")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.Front_After_C_Detection_F)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        ######### 9: Front Image After Custom Detection Label
        self.Front_After_C_Detection_L = QtWidgets.QLabel(self.Front_After_C_Detection_F)
        self.Front_After_C_Detection_L.setText("")
        self.Front_After_C_Detection_L.setPixmap(QtGui.QPixmap())
        self.Front_After_C_Detection_L.setScaledContents(True)
        self.Front_After_C_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Front_After_C_Detection_L.setObjectName("Front_After_C_Detection_L")
        self.verticalLayout_30.addWidget(self.Front_After_C_Detection_L)
        self.gridLayout_2.addWidget(self.Front_After_C_Detection_F, 0, 1, 1, 1)
        ######## 8: Back Image Before Custom Detection Frame
        self.Back_Before_C_Detection_F = QtWidgets.QFrame(self.C_Detection_Images_F)
        self.Back_Before_C_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Back_Before_C_Detection_F.setObjectName("Back_Before_C_Detection_F")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.Back_Before_C_Detection_F)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        ######### 9: Back Image Before Custom Detection Label
        self.Back_Before_C_Detection_L = QtWidgets.QLabel(self.Back_Before_C_Detection_F)
        self.Back_Before_C_Detection_L.setText("")
        self.Back_Before_C_Detection_L.setPixmap(QtGui.QPixmap())
        self.Back_Before_C_Detection_L.setScaledContents(True)
        self.Back_Before_C_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_Before_C_Detection_L.setObjectName("Back_Before_C_Detection_L")
        self.verticalLayout_29.addWidget(self.Back_Before_C_Detection_L)
        self.gridLayout_2.addWidget(self.Back_Before_C_Detection_F, 1, 0, 1, 1)
        ######## 8: Back Image After Custom Detection Frame
        self.Back_After_C_Detection_F = QtWidgets.QFrame(self.C_Detection_Images_F)
        self.Back_After_C_Detection_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Back_After_C_Detection_F.setObjectName("Back_After_C_Detection_F")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.Back_After_C_Detection_F)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        ######### 9: Back Image After Custom Detection Label
        self.Back_After_C_Detection_L = QtWidgets.QLabel(self.Back_After_C_Detection_F)
        self.Back_After_C_Detection_L.setText("")
        self.Back_After_C_Detection_L.setPixmap(QtGui.QPixmap())
        self.Back_After_C_Detection_L.setScaledContents(True)
        self.Back_After_C_Detection_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_After_C_Detection_L.setObjectName("Back_After_C_Detection_L")
        self.verticalLayout_31.addWidget(self.Back_After_C_Detection_L)
        self.gridLayout_2.addWidget(self.Back_After_C_Detection_F, 1, 1, 1, 1)
        self.verticalLayout_27.addWidget(self.C_Detection_Images_F)
        ####### 7: Custom Detection Options Frame
        self.C_Detection_Options_F = QtWidgets.QFrame(self.page_3_2)
        self.C_Detection_Options_F.setObjectName("C_Detection_Options_F")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.C_Detection_Options_F)
        self.verticalLayout_32.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        ######## 8: Custom Detection Check Boxes Frame
        self.C_Detection_Check_Boxes_F = QtWidgets.QFrame(self.C_Detection_Options_F)
        self.C_Detection_Check_Boxes_F.setStyleSheet("")
        self.C_Detection_Check_Boxes_F.setObjectName("C_Detection_Check_Boxes_F")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.C_Detection_Check_Boxes_F)
        self.gridLayout_3.setObjectName("gridLayout_3")
        ######### 9: Burn Check Box
        self.Burn_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Burn_CB.setFont(font)
        self.Burn_CB.setObjectName("Burn_CB")
        self.gridLayout_3.addWidget(self.Burn_CB, 0, 4, 1, 1)
        ######### 9: 2D Data Matrix Check Box
        self.A_2D_Data_Matrix_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.A_2D_Data_Matrix_CB.setFont(font)
        self.A_2D_Data_Matrix_CB.setObjectName("A_2D_Data_Matrix_CB")
        self.gridLayout_3.addWidget(self.A_2D_Data_Matrix_CB, 0, 0, 1, 1)
        ######### 9: Discoloration Check Box
        self.Discoloration_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Discoloration_CB.setFont(font)
        self.Discoloration_CB.setObjectName("Discoloration_CB")
        self.gridLayout_3.addWidget(self.Discoloration_CB, 1, 3, 1, 1)
        ######### 9: WWAN Card Slot Check Box
        self.Card_Slot_WWAN_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Card_Slot_WWAN_CB.setFont(font)
        self.Card_Slot_WWAN_CB.setObjectName("Card_Slot_WWAN_CB")
        self.gridLayout_3.addWidget(self.Card_Slot_WWAN_CB, 1, 2, 1, 1)
        ######### 9: Speaker Check Box
        self.Speaker_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Speaker_CB.setFont(font)
        self.Speaker_CB.setObjectName("Speaker_CB")
        self.gridLayout_3.addWidget(self.Speaker_CB, 3, 2, 1, 1)
        ######### 9: Micro SIM Check Box
        self.Micro_SIM_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Micro_SIM_CB.setFont(font)
        self.Micro_SIM_CB.setObjectName("Micro_SIM_CB")
        self.gridLayout_3.addWidget(self.Micro_SIM_CB, 2, 4, 1, 1)
        ######### 9: Bent Pins Check Box
        self.Bent_Pins_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Bent_Pins_CB.setFont(font)
        self.Bent_Pins_CB.setObjectName("Bent_Pins_CB")
        self.gridLayout_3.addWidget(self.Bent_Pins_CB, 0, 3, 1, 1)
        ######### 9: Fan Check Box
        self.Fan_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Fan_CB.setFont(font)
        self.Fan_CB.setObjectName("Fan_CB")
        self.gridLayout_3.addWidget(self.Fan_CB, 2, 0, 1, 1)
        ######### 9: WLAN Card Slot Check Box
        self.Card_Slot_WLAN_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Card_Slot_WLAN_CB.setFont(font)
        self.Card_Slot_WLAN_CB.setObjectName("Card_Slot_WLAN_CB")
        self.gridLayout_3.addWidget(self.Card_Slot_WLAN_CB, 1, 1, 1, 1)
        ######### 9: RAM Check Box
        self.RAM_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.RAM_CB.setFont(font)
        self.RAM_CB.setObjectName("RAM_CB")
        self.gridLayout_3.addWidget(self.RAM_CB, 3, 1, 1, 1)
        ######### 9: ID Block Check Box
        self.ID_Block_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.ID_Block_CB.setFont(font)
        self.ID_Block_CB.setObjectName("ID_Block_CB")
        self.gridLayout_3.addWidget(self.ID_Block_CB, 2, 2, 1, 1)
        ######### 9: HDMI Check Box
        self.HDMI_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.HDMI_CB.setFont(font)
        self.HDMI_CB.setObjectName("HDMI_CB")
        self.gridLayout_3.addWidget(self.HDMI_CB, 2, 1, 1, 1)
        ######### 9: Battery Check Box
        self.Battery_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Battery_CB.setFont(font)
        self.Battery_CB.setObjectName("Battery_CB")
        self.gridLayout_3.addWidget(self.Battery_CB, 0, 2, 1, 1)
        ######### 9: Ethernet Check Box
        self.Ethernet_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Ethernet_CB.setFont(font)
        self.Ethernet_CB.setObjectName("Ethernet_CB")
        self.gridLayout_3.addWidget(self.Ethernet_CB, 1, 4, 1, 1)
        ######### 9: Thermal Paste Check Box
        self.Thermal_Paste_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Thermal_Paste_CB.setFont(font)
        self.Thermal_Paste_CB.setObjectName("Thermal_Paste_CB")
        self.gridLayout_3.addWidget(self.Thermal_Paste_CB, 3, 3, 1, 1)
        ######### 9: USB Check Box
        self.USB_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.USB_CB.setFont(font)
        self.USB_CB.setObjectName("USB_CB")
        self.gridLayout_3.addWidget(self.USB_CB, 3, 4, 1, 1)
        ######### 9: Audio Check Box
        self.Audio_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Audio_CB.setFont(font)
        self.Audio_CB.setObjectName("Audio_CB")
        self.gridLayout_3.addWidget(self.Audio_CB, 0, 1, 1, 1)
        ######### 9: Micro SD Check Box
        self.Micro_SD_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Micro_SD_CB.setFont(font)
        self.Micro_SD_CB.setObjectName("Micro_SD_CB")
        self.gridLayout_3.addWidget(self.Micro_SD_CB, 2, 3, 1, 1)
        ######### 9: Missing Parts Check Box
        self.Missing_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Missing_CB.setFont(font)
        self.Missing_CB.setObjectName("Missing_CB")
        self.gridLayout_3.addWidget(self.Missing_CB, 3, 0, 1, 1)
        ######### 9: SSD Card Slot Check Box
        self.Card_Slot_SSD_CB = QtWidgets.QCheckBox(self.C_Detection_Check_Boxes_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Card_Slot_SSD_CB.setFont(font)
        self.Card_Slot_SSD_CB.setObjectName("Card_Slot_SSD_CB")
        self.gridLayout_3.addWidget(self.Card_Slot_SSD_CB, 1, 0, 1, 1)
        self.verticalLayout_32.addWidget(self.C_Detection_Check_Boxes_F)
        ######## 8: Custom Detection Buttons Frame
        self.C_Detection_Buttons_F = QtWidgets.QFrame(self.C_Detection_Options_F)
        self.C_Detection_Buttons_F.setObjectName("C_Detection_Buttons_F")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.C_Detection_Buttons_F)
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9.setSpacing(32)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        ######### 9: Run Custom Detection Button
        self.Run_C_Detection_B = QtWidgets.QPushButton(self.C_Detection_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Run_C_Detection_B.setFont(font)
        self.Run_C_Detection_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Run_C_Detection_B.setObjectName("Run_C_Detection_B")
        self.horizontalLayout_9.addWidget(self.Run_C_Detection_B)
        ######### 9: Check All Boxes Button
        self.Check_All_B = QtWidgets.QPushButton(self.C_Detection_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Check_All_B.setFont(font)
        self.Check_All_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Check_All_B.setObjectName("Check_All_B")
        self.horizontalLayout_9.addWidget(self.Check_All_B)
        ######### 9: Uncheck All Boxes Button
        self.Uncheck_All_B = QtWidgets.QPushButton(self.C_Detection_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Uncheck_All_B.setFont(font)
        self.Uncheck_All_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Uncheck_All_B.setObjectName("Uncheck_All_B")
        self.horizontalLayout_9.addWidget(self.Uncheck_All_B)
        ######### 9: View Images Before Custom Detection Button
        self.View_Before_C_Detection_B = QtWidgets.QPushButton(self.C_Detection_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.View_Before_C_Detection_B.setFont(font)
        self.View_Before_C_Detection_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.View_Before_C_Detection_B.setObjectName("View_Before_C_Detection_B")
        self.horizontalLayout_9.addWidget(self.View_Before_C_Detection_B)
        ######### 9: View Images After Custom Detection Button
        self.View_After_C_Detection_B = QtWidgets.QPushButton(self.C_Detection_Buttons_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.View_After_C_Detection_B.setFont(font)
        self.View_After_C_Detection_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 5px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.View_After_C_Detection_B.setObjectName("View_Before_C_Detection_B")        
        self.horizontalLayout_9.addWidget(self.View_After_C_Detection_B)        
        self.verticalLayout_32.addWidget(self.C_Detection_Buttons_F)
        self.verticalLayout_27.addWidget(self.C_Detection_Options_F, 0, QtCore.Qt.AlignBottom)
        self.stackedWidget.addWidget(self.page_3_2)
        ###### 6: Tab 3 Page 3 Stacked Widget ( 2D Data Matrix Detection Page )
        self.page_3_3 = QtWidgets.QWidget()
        self.page_3_3.setObjectName("page_3_3")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.page_3_3)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.Matrix_F = QtWidgets.QFrame(self.page_3_3)
        self.Matrix_F.setMinimumSize(QtCore.QSize(0, 450))
        self.Matrix_F.setObjectName("Matrix_F")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.Matrix_F)
        self.horizontalLayout_15.setContentsMargins(64, 1, 64, 1)
        self.horizontalLayout_15.setSpacing(64)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        ######## 8: Matrix Image Frame
        self.Matrix_Image_F = QtWidgets.QFrame(self.Matrix_F)
        self.Matrix_Image_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Matrix_Image_F.setObjectName("Matrix_Image_F")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.Matrix_Image_F)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        ######### 9: Matrix Image Label
        self.Matrix_Image_L = QtWidgets.QLabel(self.Matrix_Image_F)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Matrix_Image_L.setFont(font)
        self.Matrix_Image_L.setText("")
        self.Matrix_Image_L.setPixmap(QtGui.QPixmap())
        self.Matrix_Image_L.setScaledContents(True)
        self.Matrix_Image_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Matrix_Image_L.setObjectName("Matrix_Image_L")
        self.verticalLayout_37.addWidget(self.Matrix_Image_L)
        self.horizontalLayout_15.addWidget(self.Matrix_Image_F)
        ######## 8: Matrix Results Frame
        self.Matrix_Results_F = QtWidgets.QFrame(self.Matrix_F)
        self.Matrix_Results_F.setObjectName("Matrix_Results_F")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.Matrix_Results_F)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.Matrix_Results_Title_L = QtWidgets.QLabel(self.Matrix_Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Matrix_Results_Title_L.setFont(font)
        self.Matrix_Results_Title_L.setStyleSheet("padding: 5px;")
        self.Matrix_Results_Title_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Matrix_Results_Title_L.setObjectName("Matrix_Results_Title_L")
        self.verticalLayout_34.addWidget(self.Matrix_Results_Title_L)
        self.PPID_Recogniton_L = QtWidgets.QLabel(self.Matrix_Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.PPID_Recogniton_L.setFont(font)
        self.PPID_Recogniton_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px")
        self.PPID_Recogniton_L.setObjectName("PPID_Recogniton_L")
        self.verticalLayout_34.addWidget(self.PPID_Recogniton_L)
        self.Run_Recognition_B = QtWidgets.QPushButton(self.Matrix_Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Run_Recognition_B.setFont(font)
        self.Run_Recognition_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Run_Recognition_B.setObjectName("Run_Recognition_B")
        self.verticalLayout_34.addWidget(self.Run_Recognition_B)
        ######### 9: Save Recognition Results Button
        self.Save_Results_B = QtWidgets.QPushButton(self.Matrix_Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Save_Results_B.setFont(font)
        self.Save_Results_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Save_Results_B.setObjectName("Save_Results_B")
        self.verticalLayout_34.addWidget(self.Save_Results_B)
        self.horizontalLayout_15.addWidget(self.Matrix_Results_F, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_36.addWidget(self.Matrix_F)
        ####### 7: Manual Identification Frame
        self.Manual_Identification_F = QtWidgets.QFrame(self.page_3_3)
        self.Manual_Identification_F.setObjectName("Manual_Identification_F")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.Manual_Identification_F)
        self.verticalLayout_33.setContentsMargins(32, 1, 32, 1)
        self.verticalLayout_33.setSpacing(16)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        ######## 8: Manual Identification Title Label
        self.Manual_Identification_Title_L = QtWidgets.QLabel(self.Manual_Identification_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_Identification_Title_L.setFont(font)
        self.Manual_Identification_Title_L.setStyleSheet("padding: 5px;")
        self.Manual_Identification_Title_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Manual_Identification_Title_L.setObjectName("Manual_Identification_Title_L")
        self.verticalLayout_33.addWidget(self.Manual_Identification_Title_L, 0, QtCore.Qt.AlignTop)
        self.Manual_PPID_F = QtWidgets.QFrame(self.Manual_Identification_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Manual_PPID_F.sizePolicy().hasHeightForWidth())
        ######## 8: Manual PPID Frame
        self.Manual_PPID_F.setSizePolicy(sizePolicy)
        self.Manual_PPID_F.setObjectName("Manual_PPID_F")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.Manual_PPID_F)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        ######### 9: PPID Title Label
        self.PPID_Title_L = QtWidgets.QLabel(self.Manual_PPID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.PPID_Title_L.setFont(font)
        self.PPID_Title_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 10px")
        self.PPID_Title_L.setObjectName("PPID_Title_L")
        self.horizontalLayout_11.addWidget(self.PPID_Title_L)
        ######### 9: PPID Line Edit
        self.PPID_LE = QtWidgets.QLineEdit(self.Manual_PPID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.PPID_LE.setFont(font)
        self.PPID_LE.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    border: 2px solid rgb(30, 30, 30);\n"
        "    border-radius: 10px;\n"
        "    padding: 10px;\n"
        "}\n"
        "\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}")
        self.PPID_LE.setObjectName("PPID_LE")
        self.horizontalLayout_11.addWidget(self.PPID_LE)
        ######### 9: Save PPID Button
        self.PPID_Save_B = QtWidgets.QPushButton(self.Manual_PPID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.PPID_Save_B.setFont(font)
        self.PPID_Save_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.PPID_Save_B.setObjectName("PPID_Save_B")
        self.horizontalLayout_11.addWidget(self.PPID_Save_B)
        self.verticalLayout_33.addWidget(self.Manual_PPID_F)
        ######## 8: View Manual Entered PPID Frame
        self.View_Manual_Entered_PPID_F = QtWidgets.QFrame(self.Manual_Identification_F)
        self.View_Manual_Entered_PPID_F.setObjectName("View_Manual_Entered_PPID_F")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.View_Manual_Entered_PPID_F)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        ######### 9: Saved PPID Label
        self.Saved_PPID_L = QtWidgets.QLabel(self.View_Manual_Entered_PPID_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Saved_PPID_L.setFont(font)
        self.Saved_PPID_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px")
        self.Saved_PPID_L.setObjectName("Saved_PPID_L")
        self.horizontalLayout_12.addWidget(self.Saved_PPID_L)
        self.verticalLayout_33.addWidget(self.View_Manual_Entered_PPID_F)
        self.verticalLayout_36.addWidget(self.Manual_Identification_F, 0, QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_3_3)
        ###### 6: Tab 4 Page 1 Stacked Widget ( Generate Report Page )
        self.page_4_1 = QtWidgets.QWidget()
        self.page_4_1.setObjectName("page_4_1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_4_1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        ####### 7: Saved Results Frame
        self.Results_F = QtWidgets.QFrame(self.page_4_1)
        self.Results_F.setObjectName("Results_F")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.Results_F)
        self.verticalLayout_20.setContentsMargins(64, 1, 64, 1)
        self.verticalLayout_20.setSpacing(36)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        ######## 8: Saved Results Title Label
        self.Results_Title_L = QtWidgets.QLabel(self.Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Results_Title_L.setFont(font)
        self.Results_Title_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Results_Title_L.setObjectName("Results_Title_L")
        self.verticalLayout_20.addWidget(self.Results_Title_L)
        ######## 8: Saved Station Number Label
        self.Station_Number_Result_L = QtWidgets.QLabel(self.Results_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Station_Number_Result_L.sizePolicy().hasHeightForWidth())
        self.Station_Number_Result_L.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Station_Number_Result_L.setFont(font)
        self.Station_Number_Result_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px")
        self.Station_Number_Result_L.setObjectName("Station_Number_Result_L")
        self.verticalLayout_20.addWidget(self.Station_Number_Result_L)
        ######## 8: Saved Work ID Label
        self.Work_ID_Result_L = QtWidgets.QLabel(self.Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Work_ID_Result_L.setFont(font)
        self.Work_ID_Result_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px")
        self.Work_ID_Result_L.setObjectName("Work_ID_Result_L")
        self.verticalLayout_20.addWidget(self.Work_ID_Result_L)
        ######## 8: Saved PPID Result Label
        self.PPID_Result_L = QtWidgets.QLabel(self.Results_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.PPID_Result_L.setFont(font)
        self.PPID_Result_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px")
        self.PPID_Result_L.setObjectName("PPID_Result_L")
        self.verticalLayout_20.addWidget(self.PPID_Result_L)
        self.verticalLayout_11.addWidget(self.Results_F, 0, QtCore.Qt.AlignTop)
        ####### 7: Test and Generate Report Frame
        self.Test_And_Report_F = QtWidgets.QFrame(self.page_4_1)
        self.Test_And_Report_F.setObjectName("Test_And_Report_F")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.Test_And_Report_F)
        self.verticalLayout_21.setContentsMargins(64, 1, 64, 1)
        self.verticalLayout_21.setSpacing(16)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        ######## 8: Test and Generate Report Title Label
        self.Test_And_Report_Title_L = QtWidgets.QLabel(self.Test_And_Report_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Test_And_Report_Title_L.setFont(font)
        self.Test_And_Report_Title_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Test_And_Report_Title_L.setObjectName("Test_And_Report_Title_L")
        self.verticalLayout_21.addWidget(self.Test_And_Report_Title_L)
        ######## 8: Test Frame
        self.Test_F = QtWidgets.QFrame(self.Test_And_Report_F)
        self.Test_F.setObjectName("Test_F")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.Test_F)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        ######### 9: Test File Name Title Label
        self.Test_File_Name_Title_L = QtWidgets.QLabel(self.Test_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Test_File_Name_Title_L.setFont(font)
        self.Test_File_Name_Title_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 13px")
        self.Test_File_Name_Title_L.setObjectName("Test_File_Name_Title_L")
        self.horizontalLayout_17.addWidget(self.Test_File_Name_Title_L, 0, QtCore.Qt.AlignLeft)
        ######### 9: Test File Name Label
        self.Test_File_Name_L = QtWidgets.QLabel(self.Test_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Test_File_Name_L.sizePolicy().hasHeightForWidth())
        self.Test_File_Name_L.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Test_File_Name_L.setFont(font)
        self.Test_File_Name_L.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;\n"
        "padding: 10px\n"
        "")
        self.Test_File_Name_L.setText("")
        self.Test_File_Name_L.setObjectName("Test_File_Name_L")
        self.horizontalLayout_17.addWidget(self.Test_File_Name_L)
        ######### 9: Choose Test File Button
        self.Choose_Test_File_B = QtWidgets.QPushButton(self.Test_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Choose_Test_File_B.setFont(font)
        self.Choose_Test_File_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Choose_Test_File_B.setObjectName("Choose_Test_File_B")
        self.horizontalLayout_17.addWidget(self.Choose_Test_File_B, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_21.addWidget(self.Test_F, 0, QtCore.Qt.AlignTop)
        ######## 8: Report Frame
        self.Report_F = QtWidgets.QFrame(self.Test_And_Report_F)
        self.Report_F.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 122, 204);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "    border-radius: 10px;\n"
        "    padding: 11px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(255, 255, 255)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0, 110, 190);\n"
        "}")
        self.Report_F.setObjectName("Report_F")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.Report_F)
        self.horizontalLayout_18.setSpacing(32)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        ######### 9: Run Test File Button
        self.Run_Test_File_B = QtWidgets.QPushButton(self.Report_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Run_Test_File_B.setFont(font)
        self.Run_Test_File_B.setObjectName("Run_Test_File_B")
        self.horizontalLayout_18.addWidget(self.Run_Test_File_B)
        ######### 9: Generate Report Button
        self.Generate_Report_B = QtWidgets.QPushButton(self.Report_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Generate_Report_B.setFont(font)
        self.Generate_Report_B.setObjectName("Generate_Report_B")
        self.horizontalLayout_18.addWidget(self.Generate_Report_B)
        ######### 9: View Report Button
        self.View_Report_B = QtWidgets.QPushButton(self.Report_F)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.View_Report_B.setObjectName("View_Report_B")
        ######### 9: Send Report Button
        self.Send_Report_B = QtWidgets.QPushButton(self.View_Report_B)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Send_Report_B.setFont(font)
        self.View_Report_B.setFont(font)
        self.Send_Report_B.setObjectName(u"Send_Report_B")
        self.horizontalLayout_18.addWidget(self.View_Report_B)
        self.horizontalLayout_18.addWidget(self.Send_Report_B)
        self.verticalLayout_21.addWidget(self.Report_F)
        self.verticalLayout_11.addWidget(self.Test_And_Report_F, 0, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_4_1)
        self.horizontalLayout_8.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.Main_Body_Content)
        #### 4: Footer Container Frame
        self.Footer_Container = QtWidgets.QFrame(self.Main_Body_Container)
        self.Footer_Container.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Footer_Container.setObjectName("Footer_Container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Footer_Container)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        ##### 5: Previous Page Button Frame
        self.Previous_Page_F = QtWidgets.QFrame(self.Footer_Container)
        self.Previous_Page_F.setObjectName("Previous_Page_F")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Previous_Page_F)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        ###### 6: Previous Page Button
        self.Previous_Page_B = QtWidgets.QPushButton(self.Previous_Page_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Previous_Page_B.sizePolicy().hasHeightForWidth())
        self.Previous_Page_B.setSizePolicy(sizePolicy)
        self.Previous_Page_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0, 122, 204)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Previous_Page_B.setText("")
        ####### 7: Previous Page Button Icon
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Icons/Icons2/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Previous_Page_B.setIcon(icon15)
        self.Previous_Page_B.setIconSize(QtCore.QSize(32, 32))
        self.Previous_Page_B.setObjectName("Previous_Page_B")
        self.verticalLayout_4.addWidget(self.Previous_Page_B, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.Previous_Page_F, 0, QtCore.Qt.AlignBottom)
        ##### 5: Next Page Button Frame
        self.Next_Page_F = QtWidgets.QFrame(self.Footer_Container)
        self.Next_Page_F.setObjectName("Next_Page_F")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Next_Page_F)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        ###### 6: Next Page Button 
        self.Next_Page_B = QtWidgets.QPushButton(self.Next_Page_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Next_Page_B.sizePolicy().hasHeightForWidth())
        self.Next_Page_B.setSizePolicy(sizePolicy)
        self.Next_Page_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0, 122, 204)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Next_Page_B.setText("")
        ####### 7: Next Page Button Icon
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/Icons/Icons2/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_Page_B.setIcon(icon16)
        self.Next_Page_B.setIconSize(QtCore.QSize(32, 32))
        self.Next_Page_B.setObjectName("Next_Page_B")
        self.verticalLayout_3.addWidget(self.Next_Page_B)
        self.horizontalLayout_3.addWidget(self.Next_Page_F, 0, QtCore.Qt.AlignBottom)
        ##### 5: Size Grip Frame
        self.Size_Grip = QtWidgets.QFrame(self.Footer_Container)
        self.Size_Grip.setMinimumSize(QtCore.QSize(10, 10))
        self.Size_Grip.setMaximumSize(QtCore.QSize(10, 10))
        self.Size_Grip.setObjectName("Size_Grip")
        self.horizontalLayout_3.addWidget(self.Size_Grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.Footer_Container)
        self.horizontalLayout.addWidget(self.Main_Body_Container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## Set All The Text In The Window Function
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.App_Name_L.setText(_translate("MainWindow", "Motherboard Inspection and Testing"))
        self.Home_1A.setText(_translate("MainWindow", " Identification"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Home_P), _translate("MainWindow", "Home"))
        self.Image_Capture_Take_1B.setText(_translate("MainWindow", " Take Pictures"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Image_Capture_P), _translate("MainWindow", "Image Capture"))
        self.Detection_Normal_1B.setText(_translate("MainWindow", " Normal"))
        self.Detection_Custom_2B.setText(_translate("MainWindow", " Custom"))
        self.Detection_Matrix_3B.setText(_translate("MainWindow", " 2D Data Matrix"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Detection_P), _translate("MainWindow", "Detection"))
        self.Testing_1B.setText(_translate("MainWindow", "Generate Report"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Testing_P), _translate("MainWindow", "Testing"))
        self.Exit_B.setText(_translate("MainWindow", " Exit"))
        self.Exit_B.setShortcut(_translate("MainWindow", "Esc"))
        self.Identification_Title_L.setText(_translate("MainWindow", "User Information"))
        self.Station_Number_Title_L.setText(_translate("MainWindow", "Enter Station Number:"))
        self.Station_Number_Save_B.setText(_translate("MainWindow", "Save Station Number"))
        self.Saved_Station_Number_L.setText(_translate("MainWindow", "Saved Station Number: "))
        self.Work_ID_Title_L.setText(_translate("MainWindow", "Enter Work ID:"))
        self.Work_ID_Save_B.setText(_translate("MainWindow", "Save Work ID"))
        self.Saved_Work_ID_L.setText(_translate("MainWindow", "Saved Work ID: "))
        self.Webcam_Live_Feed_Title_L.setText(_translate("MainWindow", "Webcam Live Feed"))
        self.Capture_Options_L.setText(_translate("MainWindow", "Options"))
        self.View_Front_B.setText(_translate("MainWindow", "View Front Image"))
        self.Capture_Front_B.setText(_translate("MainWindow", "Capture Front Image"))
        self.View_Back_B.setText(_translate("MainWindow", "View Back Image"))
        self.Capture_Back_B.setText(_translate("MainWindow", "Capture Back Image"))
        self.Captured_Front_Image_L.setText(_translate("MainWindow", "Captured Front Image"))
        self.Captured_Back_Image_L.setText(_translate("MainWindow", "Captured Back Image"))
        self.Detect_Defects_B.setText(_translate("MainWindow", "Detect Defects"))
        self.Detect_2D_Data_Matrix_B.setText(_translate("MainWindow", "Detect 2D Data Matrix"))
        self.Detect_ID_Block_B.setText(_translate("MainWindow", "Detect ID Block"))
        self.Detect_All_B.setText(_translate("MainWindow", "Detect All"))
        self.Detect_IOPorts_CardSlots_B.setText(_translate("MainWindow", "Detect I/O Ports and Card Slots"))
        self.See_N_Detected_Images_B.setText(_translate("MainWindow", "See All Images"))
        self.Burn_CB.setText(_translate("MainWindow", "Burn"))
        self.A_2D_Data_Matrix_CB.setText(_translate("MainWindow", "2D Data Matrix"))
        self.Discoloration_CB.setText(_translate("MainWindow", "Discoloration"))
        self.Card_Slot_WWAN_CB.setText(_translate("MainWindow", "WWAN Card Slot"))
        self.Speaker_CB.setText(_translate("MainWindow", "Speaker"))
        self.Micro_SIM_CB.setText(_translate("MainWindow", "Micro SIM"))
        self.Bent_Pins_CB.setText(_translate("MainWindow", "Bent Pins"))
        self.Fan_CB.setText(_translate("MainWindow", "Fan"))
        self.Card_Slot_WLAN_CB.setText(_translate("MainWindow", "WLAN Card Slot"))
        self.RAM_CB.setText(_translate("MainWindow", "RAM"))
        self.ID_Block_CB.setText(_translate("MainWindow", "ID Block"))
        self.HDMI_CB.setText(_translate("MainWindow", "HDMI"))
        self.Battery_CB.setText(_translate("MainWindow", "Battery"))
        self.Ethernet_CB.setText(_translate("MainWindow", "Ethernet"))
        self.Thermal_Paste_CB.setText(_translate("MainWindow", "Thermal Paste"))
        self.USB_CB.setText(_translate("MainWindow", "USB"))
        self.Audio_CB.setText(_translate("MainWindow", "Audio"))
        self.Micro_SD_CB.setText(_translate("MainWindow", "Micro SD"))
        self.Missing_CB.setText(_translate("MainWindow", "Missing Parts"))
        self.Card_Slot_SSD_CB.setText(_translate("MainWindow", "SSD Card Slot"))
        self.Run_C_Detection_B.setText(_translate("MainWindow", "Perform Custom Detection"))
        self.Check_All_B.setText(_translate("MainWindow", "Check All"))
        self.Uncheck_All_B.setText(_translate("MainWindow", "Uncheck All"))
        self.View_Before_C_Detection_B.setText(_translate("MainWindow", "View Images Before Custom Detection"))
        self.View_After_C_Detection_B.setText(_translate("MainWindow", "View Images After Custom Detection"))
        self.Matrix_Results_Title_L.setText(_translate("MainWindow", "Detection Results"))
        self.PPID_Recogniton_L.setText(_translate("MainWindow", "PPID: "))
        self.Run_Recognition_B.setText(_translate("MainWindow", "Run Recognition"))
        self.Save_Results_B.setText(_translate("MainWindow", "Save Results"))
        self.Manual_Identification_Title_L.setText(_translate("MainWindow", "Manual Identification"))
        self.PPID_Title_L.setText(_translate("MainWindow", "Enter PPID:"))
        self.PPID_Save_B.setText(_translate("MainWindow", "Save PPID"))
        self.Saved_PPID_L.setText(_translate("MainWindow", "Saved PPID: "))
        self.Results_Title_L.setText(_translate("MainWindow", "Saved Information"))
        self.Station_Number_Result_L.setText(_translate("MainWindow", "Station Number: "))
        self.Work_ID_Result_L.setText(_translate("MainWindow", "Work ID: "))
        self.PPID_Result_L.setText(_translate("MainWindow", "PPID: "))
        self.Test_And_Report_Title_L.setText(_translate("MainWindow", "Test and Generate Report"))
        self.Test_File_Name_Title_L.setText(_translate("MainWindow", "Test File Name:"))
        self.Choose_Test_File_B.setText(_translate("MainWindow", "Select Test File"))
        self.Run_Test_File_B.setText(_translate("MainWindow", "Run Test File"))
        self.Generate_Report_B.setText(_translate("MainWindow", "Generate Report"))
        self.View_Report_B.setText(_translate("MainWindow", "View Report"))
        self.Send_Report_B.setText(_translate("MainWindow", "Send Report"))
        self.Previous_Page_B.setShortcut(_translate("MainWindow", "Left"))
        self.Next_Page_B.setShortcut(_translate("MainWindow", "Right"))

class Ui_ImageWindow(object):
    def setupUi(self, ImageWindow):
        # Image Scaling Calculations
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        Scaled_Width = int(screen_width / 1.5)
        Scaled_Height  = int(screen_height / 1.125)

        # 1: Main Window Properties
        ImageWindow.setObjectName("ImageWindow")
        ImageWindow.resize(1048, 1070)
        ImageWindow.setStyleSheet("*{\n"
        "    border: none;\n"
        "    color: rgb(167, 167, 167);\n"
        "}")

        ## 2: Central Widget Properties
        self.centralwidget = QtWidgets.QWidget(ImageWindow)
        # self.centralwidget.setMaximumSize(QtCore.QSize(1600, 1200))
        self.centralwidget.setStyleSheet("background-color: rgb(45, 45, 48);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        ### 3: Main Body Container Frame
        self.Main_Body_Container = QtWidgets.QFrame(self.centralwidget)
        self.Main_Body_Container.setObjectName("Main_Body_Container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Main_Body_Container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #### 4: Header Container Frame
        self.Header_Container = QtWidgets.QFrame(self.Main_Body_Container)
        self.Header_Container.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Header_Container.setObjectName("Header_Container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header_Container)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        ##### 5: Window Options Frame
        self.Window_Options_F = QtWidgets.QFrame(self.Header_Container)
        self.Window_Options_F.setObjectName("Window_Options_F")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Window_Options_F)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        ###### 6: Minimize Button
        self.Minimize_B = QtWidgets.QPushButton(self.Window_Options_F)
        self.Minimize_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}\n"
        "")
        self.Minimize_B.setText("")

        ####### 7: Minimize Icon 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons2/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimize_B.setIcon(icon)
        self.Minimize_B.setIconSize(QtCore.QSize(24, 24))
        self.Minimize_B.setObjectName("Minimize_B")
        self.horizontalLayout_6.addWidget(self.Minimize_B)
        
        ###### 6: Maximize Button
        self.Maximize_B = QtWidgets.QPushButton(self.Window_Options_F)
        self.Maximize_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Maximize_B.setText("")
        
        ####### 7: Maximize Icon 
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons2/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Maximize_B.setIcon(icon1)
        self.Maximize_B.setIconSize(QtCore.QSize(24, 24))
        self.Maximize_B.setObjectName("Maximize_B")
        self.horizontalLayout_6.addWidget(self.Maximize_B)
       
       ###### 6: Close Button
        self.Close_B = QtWidgets.QPushButton(self.Window_Options_F)
        self.Close_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "    padding: 2px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(62, 62, 62);\n"
        "    border: 2px solid rgb(0, 122, 204);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Close_B.setText("")
        
        ####### 7: Close Icon
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons2/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_B.setIcon(icon2)
        self.Close_B.setIconSize(QtCore.QSize(24, 24))
        self.Close_B.setObjectName("Close_B")
        self.horizontalLayout_6.addWidget(self.Close_B)
        self.horizontalLayout_2.addWidget(self.Window_Options_F, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Header_Container)
        
        #### 4: Image Container Frame
        self.Image_Container_F = QtWidgets.QFrame(self.Main_Body_Container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_Container_F.sizePolicy().hasHeightForWidth())
        self.Image_Container_F.setSizePolicy(sizePolicy)
        self.Image_Container_F.setStyleSheet("")
        self.Image_Container_F.setObjectName("Image_Container_F")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Image_Container_F)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        ##### 5: Image Frame
        self.Image_F = QtWidgets.QFrame(self.Image_Container_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_F.sizePolicy().hasHeightForWidth())
        self.Image_F.setSizePolicy(sizePolicy)
        self.Image_F.setMaximumSize(QtCore.QSize(Scaled_Width, Scaled_Height))
        self.Image_F.setStyleSheet("background-color: rgb(30, 30, 30);\n"
        "border-radius: 10px;")
        self.Image_F.setObjectName("Image_F")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Image_F)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Image_L = QtWidgets.QLabel(self.Image_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_L.sizePolicy().hasHeightForWidth())

        ##### 6: Image Label
        self.Image_L.setSizePolicy(sizePolicy)
        self.Image_L.setText("")
        self.Image_L.setPixmap(QtGui.QPixmap(""))
        self.Image_L.setScaledContents(True)
        self.Image_L.setObjectName("Image_L")
        self.horizontalLayout_7.addWidget(self.Image_L)
        self.horizontalLayout_5.addWidget(self.Image_F)
        self.verticalLayout.addWidget(self.Image_Container_F, 0, QtCore.Qt.AlignHCenter)
       
        #### 4: Footer Container Frame
        self.Footer_Container = QtWidgets.QFrame(self.Main_Body_Container)
        self.Footer_Container.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Footer_Container.setObjectName("Footer_Container")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Footer_Container)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        ##### 5: Previous Image Button Frame
        self.Previous_Image_F = QtWidgets.QFrame(self.Footer_Container)
        self.Previous_Image_F.setObjectName("Previous_Image_F")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Previous_Image_F)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Previous_Image_B = QtWidgets.QPushButton(self.Previous_Image_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Previous_Image_B.sizePolicy().hasHeightForWidth())
        
        ###### 6: Previous Image Button
        self.Previous_Image_B.setSizePolicy(sizePolicy)
        self.Previous_Image_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0, 122, 204)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Previous_Image_B.setText("")

        ####### 7: Previous Image Button Icon
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons2/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Previous_Image_B.setIcon(icon3)
        self.Previous_Image_B.setIconSize(QtCore.QSize(24, 24))
        self.Previous_Image_B.setObjectName("Previous_Image_B")
        self.verticalLayout_5.addWidget(self.Previous_Image_B, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.Previous_Image_F, 0, QtCore.Qt.AlignBottom)
        
        ##### 5: Next Image Button Frame
        self.Next_Image_F = QtWidgets.QFrame(self.Footer_Container)
        self.Next_Image_F.setObjectName("Next_Image_F")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Next_Image_F)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        ###### 6: Next Image Button 
        self.Next_Image_B = QtWidgets.QPushButton(self.Next_Image_F)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Next_Image_B.sizePolicy().hasHeightForWidth())
        self.Next_Image_B.setSizePolicy(sizePolicy)
        self.Next_Image_B.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(30, 30, 30);\n"
        "    color: rgb(167, 167, 167);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 2px solid rgb(0, 122, 204)\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(167, 167, 167);\n"
        "}")
        self.Next_Image_B.setText("")

        ####### 7: Next Page Button Icon
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons2/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_Image_B.setIcon(icon4)
        self.Next_Image_B.setIconSize(QtCore.QSize(24, 24))
        self.Next_Image_B.setObjectName("Next_Image_B")
        self.verticalLayout_6.addWidget(self.Next_Image_B)
        self.horizontalLayout_4.addWidget(self.Next_Image_F, 0, QtCore.Qt.AlignBottom)
        
        ##### 5: Size Grip Frame
        self.Window_Size_Grip = QtWidgets.QFrame(self.Footer_Container)
        self.Window_Size_Grip.setMinimumSize(QtCore.QSize(10, 10))
        self.Window_Size_Grip.setMaximumSize(QtCore.QSize(10, 10))
        self.Window_Size_Grip.setObjectName("Window_Size_Grip")
        self.horizontalLayout_4.addWidget(self.Window_Size_Grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.Footer_Container)
        self.verticalLayout_2.addWidget(self.Main_Body_Container)
        ImageWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, ImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageWindow.setWindowTitle(_translate("ImageWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ImageWindow = QtWidgets.QMainWindow()
    ImageWindow_ui = Ui_ImageWindow()
    ImageWindow_ui.setupUi(ImageWindow)
    sys.exit(app.exec_())
