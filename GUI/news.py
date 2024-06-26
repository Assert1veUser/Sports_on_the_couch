# Form implementation generated from reading ui file 'news.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(812, 511)
        Form.setMinimumSize(QtCore.QSize(750, 500))
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 500))
        self.frame_2.setMaximumSize(QtCore.QSize(800, 500))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
                                   "    image: url(res/img.png);\n"
                                   "    border-radius: 15;\n"
                                   "    border: 0px solid rgb(255, 255, 255);\n"
                                   "}\n"
                                   "QPushButton {\n"
                                   "    border: 3px solid rgb(255, 255, 255);\n"
                                   "    border-radius: 6px;\n"
                                   "    background-color:rgba(0, 0, 0, 70);\n"
                                   "    min-width: 80px;\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    font-style: bold;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#pushButton_18 {\n"
                                   "    min-width: 0px;\n"
                                   "    border: 0px solid rgb(255, 255, 255);\n"
                                   "    background-color: rgba(255, 255, 255, 0);\n"
                                   "    color: rgb(0, 0, 0);\n"
                                   "}\n"
                                   "QPushButton#pushButton_19 {\n"
                                   "    min-width: 20px;\n"
                                   "    border: 0px solid rgb(255, 255, 255);\n"
                                   "    background-color: rgba(255, 255, 255, 0);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "QWidget#scrollArea_2 {\n"
                                   "    \n"
                                   "    background-color: transparent;\n"
                                   "}\n"
                                   "QScrollArea#scrollArea {\n"
                                   "    background-color: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_19.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_19.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(30)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout.addWidget(self.pushButton_19, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_18.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.pushButton_18, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea_2 = QtWidgets.QWidget()
        self.scrollArea_2.setGeometry(QtCore.QRect(0, -1740, 773, 2200))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 2200))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 2200))
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollArea_2)
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser.setMaximumSize(QtCore.QSize(100, 30))
        palette = QtGui.QPalette()
        self.textBrowser.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 50))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        self.textBrowser_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_4.setMaximumSize(QtCore.QSize(100, 30))
        self.textBrowser_4.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_5)
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_6)
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_7.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_7.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_7)
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_8)
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_9)
        self.textBrowser_10 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_10.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_10.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_10.setFont(font)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_10)
        self.textBrowser_11 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_11.setFont(font)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_11)
        self.textBrowser_12 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_12.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_12.setFont(font)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_12)
        self.textBrowser_13 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_13.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_13.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_13.setFont(font)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_13)
        self.textBrowser_14 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_14.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_14.setFont(font)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_14)
        self.textBrowser_15 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_15.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_15.setFont(font)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_15)
        self.textBrowser_16 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_16.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_16.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_16.setFont(font)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_16)
        self.textBrowser_17 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_17.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_17.setFont(font)
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_17)
        self.textBrowser_18 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_18.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_18.setFont(font)
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_18)
        self.textBrowser_19 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_19.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_19.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_19.setFont(font)
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_19)
        self.textBrowser_20 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_20.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_20.setFont(font)
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_20)
        self.textBrowser_21 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_21.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_21.setFont(font)
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_21)
        self.textBrowser_23 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_23.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_23.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_23.setFont(font)
        self.textBrowser_23.setObjectName("textBrowser_23")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_23)
        self.textBrowser_22 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_22.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_22.setFont(font)
        self.textBrowser_22.setObjectName("textBrowser_22")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_22)
        self.textBrowser_24 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_24.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_24.setFont(font)
        self.textBrowser_24.setObjectName("textBrowser_24")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_24)
        self.textBrowser_25 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_25.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_25.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_25.setFont(font)
        self.textBrowser_25.setObjectName("textBrowser_25")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_25)
        self.textBrowser_26 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_26.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_26.setFont(font)
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_26)
        self.textBrowser_27 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_27.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_27.setFont(font)
        self.textBrowser_27.setObjectName("textBrowser_27")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_27)
        self.textBrowser_28 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_28.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_28.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_28.setFont(font)
        self.textBrowser_28.setObjectName("textBrowser_28")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_28)
        self.textBrowser_29 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_29.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_29.setFont(font)
        self.textBrowser_29.setObjectName("textBrowser_29")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_29)
        self.textBrowser_30 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_30.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_30.setFont(font)
        self.textBrowser_30.setObjectName("textBrowser_30")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_30)
        self.textBrowser_32 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_32.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_32.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_32.setFont(font)
        self.textBrowser_32.setObjectName("textBrowser_32")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_32)
        self.textBrowser_31 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_31.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_31.setFont(font)
        self.textBrowser_31.setObjectName("textBrowser_31")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_31)
        self.textBrowser_33 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_33.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_33.setFont(font)
        self.textBrowser_33.setObjectName("textBrowser_33")
        self.formLayout_2.setWidget(21, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_33)
        self.textBrowser_34 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_34.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_34.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_34.setFont(font)
        self.textBrowser_34.setObjectName("textBrowser_34")
        self.formLayout_2.setWidget(22, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_34)
        self.textBrowser_35 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_35.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_35.setFont(font)
        self.textBrowser_35.setObjectName("textBrowser_35")
        self.formLayout_2.setWidget(22, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_35)
        self.textBrowser_36 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_36.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_36.setFont(font)
        self.textBrowser_36.setObjectName("textBrowser_36")
        self.formLayout_2.setWidget(23, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_36)
        self.textBrowser_37 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_37.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_37.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_37.setFont(font)
        self.textBrowser_37.setObjectName("textBrowser_37")
        self.formLayout_2.setWidget(24, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_37)
        self.textBrowser_38 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_38.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_38.setFont(font)
        self.textBrowser_38.setObjectName("textBrowser_38")
        self.formLayout_2.setWidget(24, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_38)
        self.textBrowser_39 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_39.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_39.setFont(font)
        self.textBrowser_39.setObjectName("textBrowser_39")
        self.formLayout_2.setWidget(25, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_39)
        self.textBrowser_40 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_40.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_40.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_40.setFont(font)
        self.textBrowser_40.setObjectName("textBrowser_40")
        self.formLayout_2.setWidget(26, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_40)
        self.textBrowser_41 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_41.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_41.setFont(font)
        self.textBrowser_41.setObjectName("textBrowser_41")
        self.formLayout_2.setWidget(26, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_41)
        self.textBrowser_42 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_42.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_42.setFont(font)
        self.textBrowser_42.setObjectName("textBrowser_42")
        self.formLayout_2.setWidget(27, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_42)
        self.textBrowser_43 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_43.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_43.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_43.setFont(font)
        self.textBrowser_43.setObjectName("textBrowser_43")
        self.formLayout_2.setWidget(28, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_43)
        self.textBrowser_44 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_44.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_44.setFont(font)
        self.textBrowser_44.setObjectName("textBrowser_44")
        self.formLayout_2.setWidget(28, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_44)
        self.textBrowser_45 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_45.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_45.setFont(font)
        self.textBrowser_45.setObjectName("textBrowser_45")
        self.formLayout_2.setWidget(29, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_45)
        self.textBrowser_46 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_46.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_46.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_46.setFont(font)
        self.textBrowser_46.setObjectName("textBrowser_46")
        self.formLayout_2.setWidget(30, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_46)
        self.textBrowser_47 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_47.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_47.setFont(font)
        self.textBrowser_47.setObjectName("textBrowser_47")
        self.formLayout_2.setWidget(30, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_47)
        self.textBrowser_48 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_48.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_48.setFont(font)
        self.textBrowser_48.setObjectName("textBrowser_48")
        self.formLayout_2.setWidget(31, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_48)
        self.textBrowser_49 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_49.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_49.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_49.setFont(font)
        self.textBrowser_49.setObjectName("textBrowser_49")
        self.formLayout_2.setWidget(32, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_49)
        self.textBrowser_50 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_50.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_50.setFont(font)
        self.textBrowser_50.setObjectName("textBrowser_50")
        self.formLayout_2.setWidget(32, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_50)
        self.textBrowser_51 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_51.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_51.setFont(font)
        self.textBrowser_51.setObjectName("textBrowser_51")
        self.formLayout_2.setWidget(33, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_51)
        self.textBrowser_52 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_52.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_52.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_52.setFont(font)
        self.textBrowser_52.setObjectName("textBrowser_52")
        self.formLayout_2.setWidget(34, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_52)
        self.textBrowser_53 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_53.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_53.setFont(font)
        self.textBrowser_53.setObjectName("textBrowser_53")
        self.formLayout_2.setWidget(34, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_53)
        self.textBrowser_54 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_54.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_54.setFont(font)
        self.textBrowser_54.setObjectName("textBrowser_54")
        self.formLayout_2.setWidget(35, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_54)
        self.textBrowser_55 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_55.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_55.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_55.setFont(font)
        self.textBrowser_55.setObjectName("textBrowser_55")
        self.formLayout_2.setWidget(36, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_55)
        self.textBrowser_56 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_56.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_56.setFont(font)
        self.textBrowser_56.setObjectName("textBrowser_56")
        self.formLayout_2.setWidget(36, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_56)
        self.textBrowser_57 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_57.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_57.setFont(font)
        self.textBrowser_57.setObjectName("textBrowser_57")
        self.formLayout_2.setWidget(37, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_57)
        self.textBrowser_58 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_58.setMinimumSize(QtCore.QSize(100, 30))
        self.textBrowser_58.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        self.textBrowser_58.setFont(font)
        self.textBrowser_58.setObjectName("textBrowser_58")
        self.formLayout_2.setWidget(38, QtWidgets.QFormLayout.ItemRole.LabelRole, self.textBrowser_58)
        self.textBrowser_59 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_59.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_59.setFont(font)
        self.textBrowser_59.setObjectName("textBrowser_59")
        self.formLayout_2.setWidget(38, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_59)
        self.textBrowser_60 = QtWidgets.QTextBrowser(parent=self.scrollArea_2)
        self.textBrowser_60.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.textBrowser_60.setFont(font)
        self.textBrowser_60.setObjectName("textBrowser_60")
        self.formLayout_2.setWidget(39, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_60)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.scrollArea.setWidget(self.scrollArea_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_19.setText(_translate("Form", "🠔"))
        self.pushButton_18.setText(_translate("Form", ""))
