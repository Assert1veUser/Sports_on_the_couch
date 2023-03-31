from PyQt6 import QtWidgets, QtGui
from qtpy import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('res/label.png'))
        self.setLayout(QVBoxLayout())
        self.add_w1()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(1000, 500)
        self.show()

    def add_w1(self):
        w = Widget1()
        w.pushButton_5.clicked.connect(self.close)
        w.pushButton_2.clicked.connect(self.click_table)
        self.layout().addWidget(w)

    def add_w2(self):
        w2 = Widget_table()
        w2.pushButton.clicked.connect(self.close)
        w2.pushButton_2.clicked.connect(self.click_start)
        self.layout().addWidget(w2)


    def click_table(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w2()

    def click_start(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w1()

    def del_w(self, w):
        w.deleteLater()


class Widget1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/first.ui", self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()


class Widget_table(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/second_1.ui", self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()
