# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\titou\PycharmProjects\info_jetpack\GamePage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

import Objects as obj

from tkinter import *

class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(1280, 720)
        Game.setMinimumSize(QtCore.QSize(1280, 720))
        Game.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(Game)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 540, 71, 71))
        self.label_2.setStyleSheet("\n"
                                   "background-image: url(:/newPrefix/personnage.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("personnage.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fond.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.lineEdit.setStyleSheet("color: rgb(85, 255, 255);\n"
                                    "background-color: rgb(85, 255, 127,0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        Game.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        Game.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Game)
        self.statusbar.setObjectName("statusbar")
        Game.setStatusBar(self.statusbar)

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "MainWindow"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QMainWindow()
    ui = Ui_Game()

    ui.setupUi(Game)
    Game.show()


    def quelletouche():
        print(ui.lineEdit.text())
        ui.lineEdit.setText("")


    ui.lineEdit.textChanged.connect(quelletouche)

    sys.exit(app.exec_())
