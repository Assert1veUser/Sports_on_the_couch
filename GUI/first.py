from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QtCore.QSize(800, 500))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setMinimumSize(QtCore.QSize(800, 500))
        self.frame.setMaximumSize(QtCore.QSize(800, 500))
        self.frame.setStyleSheet("QFrame#frame{\n"
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
                                 "QPushButton#pushButton_5 {\n"
                                 "    min-width: 0px;\n"
                                 "    border: 0px solid rgb(255, 255, 255);\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "    color: rgb(0, 0, 0);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                 "}\n"
                                 "QPushButton#pushButton_5:pressed {\n"
                                 "    color: rgba(0, 0, 0, 70);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:flat {\n"
                                 "    border: none; /* no border for a flat push button */\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:default {\n"
                                 "    border-color: navy; /* make the default button prominent */\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 5, 5, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_5.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.widget = QtWidgets.QWidget(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy
                                           .Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(-1, 180, -1, -1)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(86, 40))
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
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
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
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(86, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
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
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt
                                        .AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Новости"))
        self.pushButton_2.setText(_translate("Form", "Таблица"))
        self.pushButton_3.setText(_translate("Form", "Матчи"))
        self.pushButton_4.setText(_translate("Form", "Команды"))
