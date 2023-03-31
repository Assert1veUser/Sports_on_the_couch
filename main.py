import sys
from tkinter.ttk import Frame
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from qtpy import QtCore
import subprocess
from DataBase import Create_DataBase

from GUI.Sotc_gui import Widget


def main():
    app = QApplication(sys.argv)
    main_gw = Widget()


    app.exec()


if __name__ == "__main__":
    main()
