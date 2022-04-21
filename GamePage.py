# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\titou\PycharmProjects\info_jetpack\GamePage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(1080, 720)
        Game.setMinimumSize(QtCore.QSize(1080, 720))
        Game.setMaximumSize(QtCore.QSize(2100, 720))
        self.centralwidget = QtWidgets.QWidget(Game)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        self.label.setMinimumSize(QtCore.QSize(1080, 720))
        self.label.setMaximumSize(QtCore.QSize(1080, 720))
        self.label.setPixmap(QtGui.QPixmap("image/fond.png"))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, main.player.y, 80, 80))
        self.label_2.setStyleSheet("\n"
"background-image: url(:/newPrefix/personnage.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/personnage.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Game.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
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


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QMainWindow()
    ui = Ui_Game()
    ui.setupUi(Game)
    Game.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QMainWindow()
    ui = Ui_Game()
    ui.setupUi(Game)
    Game.show()
    sys.exit(app.exec_())
