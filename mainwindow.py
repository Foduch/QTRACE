# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DownloadRaces = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadRaces.setObjectName("DownloadRaces")
        self.horizontalLayout.addWidget(self.DownloadRaces)
        self.set_number_butt = QtWidgets.QPushButton(self.centralwidget)
        self.set_number_butt.setObjectName("set_number_butt")
        self.horizontalLayout.addWidget(self.set_number_butt)
        self.refereeing_butt = QtWidgets.QPushButton(self.centralwidget)
        self.refereeing_butt.setObjectName("refereeing_butt")
        self.horizontalLayout.addWidget(self.refereeing_butt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DownloadRaces.setText(_translate("MainWindow", "Загрузить гонки"))
        self.set_number_butt.setText(_translate("MainWindow", "Выдача номеров"))
        self.refereeing_butt.setText(_translate("MainWindow", "Судейство"))

