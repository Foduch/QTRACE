import os
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from classes.ClassApi import *
from classes.ClassDB import *
from classes.ClassRace import *
from classes.ClassRacer import *
from messages import *
import mainwindow

class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.DownloadRaces.clicked.connect(self.download_races)
        self.set_number_butt.clicked.connect(self.show_guid)
        self.show_races()
        db = Database()
        self.races=db.get_races()

    def show_races(self):
        self.listWidget.clear()
        db = Database()
        try:
            self.races = db.get_races()
        except:
            pass
        for race in self.races:
            self.listWidget.addItem(str(race))

    def download_races(self):
        self.races = api.get_races()
        db = Database()
        db.insert_races(self.races)
        self.show_races()

    def show_guid(self):
        print(self.races[self.listWidget.currentRow()].get_id())
        print(str(self.races[self.listWidget.currentRow()]))



def main():
    global api
    global ZELBIKE_ACCESS_KEY
    try:
        ZELBIKE_ACCESS_KEY = os.environ['ZELBIKE_ACCESS_KEY']
    except:
        ZELBIKE_ACCESS_KEY = input(MESSAGE_ENTER_ZELBIKE_ACCESS_KEY)
    api = Api('Zelbike', 'http://api.chrono.zelbike.ru/v1/RaceStages/')
    api.key = ZELBIKE_ACCESS_KEY

    db = Database()
    db.create_tables()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()