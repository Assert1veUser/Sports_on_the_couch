# Form implementation generated from reading ui file 'teams.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 496)
        Form.setStyleSheet("QWidget#Form{\n"
"    image: url(res/img.png);\n"
"    border-radius: 15;\n"
"    border: 0px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton#pushButton_18 {\n"
"    min-width: 0px;\n"
"    border: 0px solid rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_19 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout.addWidget(self.pushButton_19)
        self.pushButton_18 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_18.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.pushButton_18)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 9, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setIconSize(QtCore.QSize(12, 12))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 4, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 6, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 8, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 10, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem8, 2, 9, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem9, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem10, 3, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem11, 3, 4, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_7.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_7.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 6, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem12, 3, 8, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_17.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_17.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("")
        self.pushButton_17.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 3, 9, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem13, 3, 10, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem14, 4, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem15, 5, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_14.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_14.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("")
        self.pushButton_14.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 5, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem16, 5, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_13.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_13.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 5, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem17, 5, 4, 1, 2)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_12.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_12.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 5, 6, 1, 2)
        spacerItem18 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem18, 5, 8, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_9.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_9.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 5, 9, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem19, 5, 10, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem20, 6, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_8.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_8.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 6, 5, 1, 2)
        spacerItem21 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem21, 7, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_10.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_10.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 7, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_11.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_11.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 7, 6, 2, 1)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_16.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_16.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("")
        self.pushButton_16.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 7, 7, 1, 2)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_15.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_15.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 8, 3, 1, 2)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_19.setText(_translate("Form", "PushButton"))
        self.pushButton_18.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Новости"))
        self.pushButton_2.setText(_translate("Form", "Новости"))
        self.pushButton_3.setText(_translate("Form", "Новости"))
        self.pushButton_4.setText(_translate("Form", "Новости"))
        self.pushButton_5.setText(_translate("Form", "Новости"))
        self.pushButton_6.setText(_translate("Form", "Новости"))
        self.pushButton_7.setText(_translate("Form", "Новости"))
        self.pushButton_17.setText(_translate("Form", "Новости"))
        self.pushButton_14.setText(_translate("Form", "Новости"))
        self.pushButton_13.setText(_translate("Form", "Новости"))
        self.pushButton_12.setText(_translate("Form", "Новости"))
        self.pushButton_9.setText(_translate("Form", "Новости"))
        self.pushButton_8.setText(_translate("Form", "Новости"))
        self.pushButton_10.setText(_translate("Form", "Новости"))
        self.pushButton_11.setText(_translate("Form", "Новости"))
        self.pushButton_16.setText(_translate("Form", "Новости"))
        self.pushButton_15.setText(_translate("Form", "Новости"))