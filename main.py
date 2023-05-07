import asyncio
import sys
from tkinter.ttk import Frame
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from qtpy import QtCore
import subprocess

import DataBase.Create_DataBase
import Model

from DataBase import Create_DataBase

from GUI.Sotc_gui import Widget


def main():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(Model.Parsing.team_pars())
    app = QApplication(sys.argv)
    DataBase.Create_DataBase.Select_standings()
    DataBase.Create_DataBase.Select_calendar()
    DataBase.Create_DataBase.Select_teams()
    DataBase.Create_DataBase.Select_news()

    main_gw = Widget()


    app.exec()


if __name__ == "__main__":
    main()
