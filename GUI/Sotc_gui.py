from PyQt6 import QtWidgets, QtGui
from PyQt6.uic.properties import QtCore
from qtpy import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QTextEdit, QLineEdit

import DataBase.Create_DataBase
import GUI.second_1
from GUI.second_1 import Ui_Form


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
        w.pushButton_3.clicked.connect(self.click_calendar)
        w.pushButton_4.clicked.connect(self.click_teams)
        w.pushButton.clicked.connect(self.click_news)
        self.layout().addWidget(w)

    def add_w2(self):
        w2 = Widget_table()
        w2.pushButton.clicked.connect(self.close)
        w2.pushButton_2.clicked.connect(self.click_start)
        self.layout().addWidget(w2)

    def add_w3(self):
        w3 = Widget_calendar()
        w3.pushButton_4.clicked.connect(self.close)
        w3.pushButton_3.clicked.connect(self.click_start)
        self.layout().addWidget(w3)

    def add_w4(self):
        w4 = Widget_teams()
        w4.pushButton_18.clicked.connect(self.close)
        w4.pushButton_19.clicked.connect(self.click_start)
        w4.pushButton_1.clicked.connect(self.click_team1)
        w4.pushButton_2.clicked.connect(self.click_team2)
        w4.pushButton_3.clicked.connect(self.click_team3)
        w4.pushButton_4.clicked.connect(self.click_team4)
        w4.pushButton_5.clicked.connect(self.click_team5)
        w4.pushButton_6.clicked.connect(self.click_team6)
        w4.pushButton_7.clicked.connect(self.click_team7)
        w4.pushButton_8.clicked.connect(self.click_team8)
        w4.pushButton_9.clicked.connect(self.click_team9)
        w4.pushButton_10.clicked.connect(self.click_team10)
        w4.pushButton_11.clicked.connect(self.click_team11)
        w4.pushButton_12.clicked.connect(self.click_team12)
        w4.pushButton_13.clicked.connect(self.click_team13)
        w4.pushButton_14.clicked.connect(self.click_team14)
        w4.pushButton_15.clicked.connect(self.click_team15)
        w4.pushButton_16.clicked.connect(self.click_team16)
        self.layout().addWidget(w4)

    def add_w5(self, a):
        w5 = Widget_teamInfo(a)
        w5.pushButton_18.clicked.connect(self.close)
        w5.pushButton_19.clicked.connect(self.click_back)
        self.layout().addWidget(w5)

    def add_w6(self):
        w6 = Widget_news()
        w6.pushButton_18.clicked.connect(self.close)
        w6.pushButton_19.clicked.connect(self.click_start)
        self.layout().addWidget(w6)

    def click_table(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w2()

    def click_start(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w1()

    def click_back(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w4()

    def click_calendar(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w3()

    def click_teams(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w4()

    def click_news(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w6()


    def click_team1(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(0)

    def click_team2(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(1)

    def click_team3(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(2)

    def click_team4(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(3)

    def click_team5(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(4)

    def click_team6(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(5)

    def click_team7(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(6)

    def click_team8(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(7)

    def click_team9(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(8)

    def click_team10(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(9)

    def click_team11(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(10)

    def click_team12(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(11)

    def click_team13(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(12)

    def click_team14(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(13)

    def click_team15(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(14)

    def click_team16(self):
        self.del_w(self.layout().itemAt(0).widget())
        self.add_w5(15)

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

        table = self.tableWidget

        table.setRowCount(16)
        table.setColumnCount(11)
        table.setHorizontalHeaderLabels(("Команда", "ВИ", "ВВ", "ВН", "ВП", "ДВ", "ДН", "ДП", "ГВ", "ГН",
                                         "ГП"))

        for i in range(0, 16):
            table.setItem(i, 0, QTableWidgetItem(DataBase.Create_DataBase.standingsName[i]))
            table.setItem(i, 1, QTableWidgetItem(DataBase.Create_DataBase.standingsGA[i]))
            table.setItem(i, 2, QTableWidgetItem(DataBase.Create_DataBase.standingsWA[i]))
            table.setItem(i, 3, QTableWidgetItem(DataBase.Create_DataBase.standingsDA[i]))
            table.setItem(i, 4, QTableWidgetItem(DataBase.Create_DataBase.standingsDeA[i]))
            table.setItem(i, 5, QTableWidgetItem(DataBase.Create_DataBase.standingsWH[i]))
            table.setItem(i, 6, QTableWidgetItem(DataBase.Create_DataBase.standingsDH[i]))
            table.setItem(i, 7, QTableWidgetItem(DataBase.Create_DataBase.standingsDeH[i]))
            table.setItem(i, 8, QTableWidgetItem(DataBase.Create_DataBase.standingsWV[i]))
            table.setItem(i, 9, QTableWidgetItem(DataBase.Create_DataBase.standingsDV[i]))
            table.setItem(i, 10, QTableWidgetItem(DataBase.Create_DataBase.standingsDeV[i]))

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()


class Widget_calendar(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/second_calendar.ui", self)

        table = self.tableWidget

        table.setRowCount(8)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(("Команды", "Счет", "Дата игры", "Стадион", "Коэф. победы", "Коэф. нечьи",
                                         "Коэф. поражения"))

        for i in range(0, 8):
            table.setItem(i, 0, QTableWidgetItem(DataBase.Create_DataBase.calendarName[i]))
            table.setItem(i, 1, QTableWidgetItem(DataBase.Create_DataBase.calendarScore[i]))
            table.setItem(i, 2, QTableWidgetItem(DataBase.Create_DataBase.calendarDate[i]))
            table.setItem(i, 3, QTableWidgetItem(DataBase.Create_DataBase.calendarStadium[i]))
            table.setItem(i, 4, QTableWidgetItem(DataBase.Create_DataBase.calendarWin_first[i]))
            table.setItem(i, 5, QTableWidgetItem(DataBase.Create_DataBase.calendarDraw[i]))
            table.setItem(i, 6, QTableWidgetItem(DataBase.Create_DataBase.calendarWin_second[i]))

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()


class Widget_teams(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/teams.ui", self)

        button_1 = self.pushButton_1
        button_2 = self.pushButton_2
        button_3 = self.pushButton_3
        button_4 = self.pushButton_4
        button_5 = self.pushButton_5
        button_6 = self.pushButton_6
        button_7 = self.pushButton_7
        button_8 = self.pushButton_8
        button_9 = self.pushButton_9
        button_10 = self.pushButton_10
        button_11 = self.pushButton_11
        button_12 = self.pushButton_12
        button_13 = self.pushButton_13
        button_14 = self.pushButton_14
        button_15 = self.pushButton_15
        button_16 = self.pushButton_16

        button_1.setText(DataBase.Create_DataBase.teamsName[0])
        button_2.setText(DataBase.Create_DataBase.teamsName[1])
        button_3.setText(DataBase.Create_DataBase.teamsName[2])
        button_4.setText(DataBase.Create_DataBase.teamsName[3])
        button_5.setText(DataBase.Create_DataBase.teamsName[4])
        button_6.setText(DataBase.Create_DataBase.teamsName[5])
        button_7.setText(DataBase.Create_DataBase.teamsName[6])
        button_8.setText(DataBase.Create_DataBase.teamsName[7])
        button_9.setText(DataBase.Create_DataBase.teamsName[8])
        button_10.setText(DataBase.Create_DataBase.teamsName[9])
        button_11.setText(DataBase.Create_DataBase.teamsName[10])
        button_12.setText(DataBase.Create_DataBase.teamsName[11])
        button_13.setText(DataBase.Create_DataBase.teamsName[12])
        button_14.setText(DataBase.Create_DataBase.teamsName[13])
        button_15.setText(DataBase.Create_DataBase.teamsName[14])
        button_16.setText(DataBase.Create_DataBase.teamsName[15])

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()


class Widget_teamInfo(QWidget):
    def __init__(self, a):
        super().__init__()
        uic.loadUi("GUI/team_1.ui", self)

        table = self.tableWidget

        table.setRowCount(13)
        table.setColumnCount(2)

        table.setColumnWidth(0, 200)
        table.setColumnWidth(1, 370)

        table.setHorizontalHeaderLabels(("Название", "Значение"))

        table.setItem(0, 0, QTableWidgetItem("Официальное название"))
        table.setItem(1, 0, QTableWidgetItem("Город"))
        table.setItem(2, 0, QTableWidgetItem("Год основания"))
        table.setItem(3, 0, QTableWidgetItem("Стадион"))
        table.setItem(4, 0, QTableWidgetItem("Главный тренер"))
        table.setItem(5, 0, QTableWidgetItem("Сезонов в премьер лиге"))
        table.setItem(6, 0, QTableWidgetItem("Игр в премьер лиге"))
        table.setItem(7, 0, QTableWidgetItem("Побед"))
        table.setItem(8, 0, QTableWidgetItem("Ничьих"))
        table.setItem(9, 0, QTableWidgetItem("Поражений"))
        table.setItem(10, 0, QTableWidgetItem("Забитых мячей"))
        table.setItem(11, 0, QTableWidgetItem("Пропущенных мячей"))
        table.setItem(12, 0, QTableWidgetItem("Сухих матчей"))

        add_info(a, table)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()


class Widget_news(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/news.ui", self)

        text = self.textBrowser
        text.setText(DataBase.Create_DataBase.newsDate[0])

        text2 = self.textBrowser_2
        text2.setText(DataBase.Create_DataBase.newsTitle[0])

        text3 = self.textBrowser_3
        text3.setText(DataBase.Create_DataBase.newsMain_text[0])

        text4 = self.textBrowser_4
        text4.setText(DataBase.Create_DataBase.newsDate[1])

        text5 = self.textBrowser_5
        text5.setText(DataBase.Create_DataBase.newsTitle[1])

        text6 = self.textBrowser_6
        text6.setText(DataBase.Create_DataBase.newsMain_text[1])

        text7 = self.textBrowser_7
        text7.setText(DataBase.Create_DataBase.newsDate[2])

        text8 = self.textBrowser_8
        text8.setText(DataBase.Create_DataBase.newsTitle[2])

        text9 = self.textBrowser_9
        text9.setText(DataBase.Create_DataBase.newsMain_text[2])

        text10 = self.textBrowser_10
        text10.setText(DataBase.Create_DataBase.newsDate[3])

        text11 = self.textBrowser_11
        text11.setText(DataBase.Create_DataBase.newsTitle[3])

        text12 = self.textBrowser_12
        text12.setText(DataBase.Create_DataBase.newsMain_text[3])

        text13 = self.textBrowser_13
        text13.setText(DataBase.Create_DataBase.newsDate[4])

        text14 = self.textBrowser_14
        text14.setText(DataBase.Create_DataBase.newsTitle[4])

        text15 = self.textBrowser_15
        text15.setText(DataBase.Create_DataBase.newsMain_text[4])

        text16 = self.textBrowser_16
        text16.setText(DataBase.Create_DataBase.newsDate[5])

        text17 = self.textBrowser_17
        text17.setText(DataBase.Create_DataBase.newsTitle[5])

        text18 = self.textBrowser_18
        text18.setText(DataBase.Create_DataBase.newsMain_text[5])

        text19 = self.textBrowser_19
        text19.setText(DataBase.Create_DataBase.newsDate[6])

        text20 = self.textBrowser_20
        text20.setText(DataBase.Create_DataBase.newsTitle[6])

        text21 = self.textBrowser_21
        text21.setText(DataBase.Create_DataBase.newsMain_text[6])

        text22 = self.textBrowser_22
        text22.setText(DataBase.Create_DataBase.newsTitle[7])

        text23 = self.textBrowser_23
        text23.setText(DataBase.Create_DataBase.newsDate[7])

        text24 = self.textBrowser_24
        text24.setText(DataBase.Create_DataBase.newsMain_text[7])

        text25 = self.textBrowser_25
        text25.setText(DataBase.Create_DataBase.newsDate[8])

        text26 = self.textBrowser_26
        text26.setText(DataBase.Create_DataBase.newsTitle[8])

        text27 = self.textBrowser_27
        text27.setText(DataBase.Create_DataBase.newsMain_text[8])

        text28 = self.textBrowser_28
        text28.setText(DataBase.Create_DataBase.newsDate[9])

        text29 = self.textBrowser_29
        text29.setText(DataBase.Create_DataBase.newsTitle[9])

        text30 = self.textBrowser_30
        text30.setText(DataBase.Create_DataBase.newsMain_text[9])

        text31 = self.textBrowser_31
        text31.setText(DataBase.Create_DataBase.newsTitle[10])

        text32 = self.textBrowser_32
        text32.setText(DataBase.Create_DataBase.newsDate[10])

        text33 = self.textBrowser_33
        text33.setText(DataBase.Create_DataBase.newsMain_text[10])

        text34 = self.textBrowser_34
        text34.setText(DataBase.Create_DataBase.newsDate[11])

        text35 = self.textBrowser_35
        text35.setText(DataBase.Create_DataBase.newsTitle[11])

        text36 = self.textBrowser_36
        text36.setText(DataBase.Create_DataBase.newsMain_text[11])

        text37 = self.textBrowser_37
        text37.setText(DataBase.Create_DataBase.newsDate[12])

        text38 = self.textBrowser_38
        text38.setText(DataBase.Create_DataBase.newsTitle[12])

        text39 = self.textBrowser_39
        text39.setText(DataBase.Create_DataBase.newsMain_text[12])

        text40 = self.textBrowser_40
        text40.setText(DataBase.Create_DataBase.newsDate[13])

        text41 = self.textBrowser_41
        text41.setText(DataBase.Create_DataBase.newsTitle[13])

        text42 = self.textBrowser_42
        text42.setText(DataBase.Create_DataBase.newsMain_text[13])

        text43 = self.textBrowser_43
        text43.setText(DataBase.Create_DataBase.newsDate[14])

        text44 = self.textBrowser_44
        text44.setText(DataBase.Create_DataBase.newsTitle[14])

        text45 = self.textBrowser_45
        text45.setText(DataBase.Create_DataBase.newsMain_text[14])

        text46 = self.textBrowser_46
        text46.setText(DataBase.Create_DataBase.newsDate[15])

        text47 = self.textBrowser_47
        text47.setText(DataBase.Create_DataBase.newsTitle[15])

        text48 = self.textBrowser_48
        text48.setText(DataBase.Create_DataBase.newsMain_text[15])

        text49 = self.textBrowser_49
        text49.setText(DataBase.Create_DataBase.newsDate[16])

        text50 = self.textBrowser_50
        text50.setText(DataBase.Create_DataBase.newsTitle[16])

        text51 = self.textBrowser_51
        text51.setText(DataBase.Create_DataBase.newsMain_text[16])

        text52 = self.textBrowser_52
        text52.setText(DataBase.Create_DataBase.newsDate[17])

        text53 = self.textBrowser_53
        text53.setText(DataBase.Create_DataBase.newsTitle[17])

        text54 = self.textBrowser_54
        text54.setText(DataBase.Create_DataBase.newsMain_text[17])

        text55 = self.textBrowser_55
        text55.setText(DataBase.Create_DataBase.newsDate[18])

        text56 = self.textBrowser_56
        text56.setText(DataBase.Create_DataBase.newsTitle[18])

        text57 = self.textBrowser_57
        text57.setText(DataBase.Create_DataBase.newsMain_text[18])

        text58 = self.textBrowser_58
        text58.setText(DataBase.Create_DataBase.newsDate[19])

        text59 = self.textBrowser_59
        text59.setText(DataBase.Create_DataBase.newsTitle[19])

        text60 = self.textBrowser_60
        text60.setText(DataBase.Create_DataBase.newsMain_text[19])





        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()


def add_info(a, self):
    self.setItem(0, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsName[a]))
    self.setItem(1, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsCity[a]))
    self.setItem(2, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsYear_foundation[a]))
    self.setItem(3, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsStadium[a]))
    self.setItem(4, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsHead_coach[a]))
    self.setItem(5, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsSeasons_league[a]))
    self.setItem(6, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsGames_league[a]))
    self.setItem(7, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsWins[a]))
    self.setItem(8, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsDraws[a]))
    self.setItem(9, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsDefeats[a]))
    self.setItem(10, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsGoals_scored[a]))
    self.setItem(11, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsMissed_scored[a]))
    self.setItem(12, 1, QTableWidgetItem(DataBase.Create_DataBase.teamsDry_matches[a]))
