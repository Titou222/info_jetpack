# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\titou\PycharmProjects\info_jetpack\GamePage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Objects as obj



class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1280, 720)
        Main.setMinimumSize(QtCore.QSize(1280, 720))
        Main.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 1280, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fond.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.pushButton.setStyleSheet("color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.pushButton.setText(_translate("Main", "START TO PLAY"))

class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(1080, 720)
        Game.setMinimumSize(QtCore.QSize(1280, 720))
        Game.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(Game)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("Sansation")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(170, 170, 255);\n"
"background-color: rgb(85, 170, 0,0);")
        self.pushButton.setObjectName("pushButton")

        self.label_perso = QtWidgets.QLabel(self.centralwidget)
        self.label_perso.setGeometry(QtCore.QRect(20, 600, 50, 50))
        self.label_perso.setStyleSheet("\n"
"background-image: url(:personnage.png);")
        self.label_perso.setText("")
        self.label_perso.setPixmap(QtGui.QPixmap("personnage.png"))
        self.label_perso.setScaledContents(True)
        self.label_perso.setObjectName("label_2")

        self.label_fond = QtWidgets.QLabel(self.centralwidget)
        self.label_fond.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label_fond.setStyleSheet("")
        self.label_fond.setText("")
        self.label_fond.setPixmap(QtGui.QPixmap("fond.png"))
        self.label_fond.setObjectName("label")
        self.label_fond.raise_()
        self.pushButton.raise_()
        self.label_perso.raise_()
        Game.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 720))
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
        self.pushButton.setText(_translate("Game", "CLICK HERE"))





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QMainWindow()
    Game_ui = Ui_Game()
    Game_ui.setupUi(Game)
    Game.show()

    life = 3
    xini = 20
    yini = 600
    player = obj.Player(life, xini, yini, Game_ui)


    def jump():
        player.y = 200
        Game_ui.label_perso.setGeometry(QtCore.QRect(20, player.y, 50, 50))
        Game.show()


    Game_ui.pushButton.clicked.connect(jump)
    sys.exit(app.exec_())
