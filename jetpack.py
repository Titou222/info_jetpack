from PyQt5 import QtCore, QtGui, QtWidgets
from MainPage import Ui_Main
from GamePage import Ui_Game
import sys
import Objects as obj
import time



#slots
def afficheMain():
    Main.show()
def afficheGame():
    t0 = time.time()
    Game.show()
    Main.close()

def quelletouche():

    if Game_ui.lineEdit.text() == " ":
        #action que tu veux qu'il fasse ducoup jump dans ton cas
        jump()
    Game_ui.lineEdit.setText("")


def jump(): #à mettre dans player par la suite
    player.y = 200
    Game_ui.label_2.setGeometry(QtCore.QRect(20, player.y, 50, 50))

#création de l'appli (Main)
app = QtWidgets.QApplication(sys.argv)
Main = QtWidgets.QMainWindow()
ui = Ui_Main()
ui.setupUi(Main)

#Création de la boite de dialogue Game
Game = QtWidgets.QMainWindow()
Game_ui = Ui_Game()
Game_ui.setupUi(Game)

Main.show()

#Les signaux
ui.pushButton.clicked.connect(afficheGame)
Game_ui.lineEdit.textChanged.connect(quelletouche)

#Création du joueur
life = 3
xini = 20
yini = 600
player = obj.Player(life, xini, yini, ui)




sys.exit(app.exec_())