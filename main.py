import sys
from PyQt6.QtWidgets import QApplication
import DataBase.Create_DataBase
from GUI.Sotc_gui import Widget


def main():
    app = QApplication(sys.argv)
    DataBase.Create_DataBase.Select_standings()
    DataBase.Create_DataBase.Select_calendar()
    DataBase.Create_DataBase.Select_teams()
    DataBase.Create_DataBase.Select_news()

    main_gw = Widget()

    app.exec()


if __name__ == "__main__":
    main()
