import pygame
from Game import Game
pygame.init()


#define a clock
clock = pygame.time.Clock()
FPS = 60

#generate the window of the game
pygame.display.set_caption("Jetpack")

screen_size_x = 1280
screen_size_y = 720
screen = pygame.display.set_mode((screen_size_x,screen_size_y))


#import background
background = pygame.image.load("assets/bg.jpg")

#import banner
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() // 4

#import button
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() // 3.33
play_button_rect.y = screen.get_width() // 3.5
#load our game
game = Game()


running = True

while running:
    #apply background
    screen.blit(background, (0,-200))

    #check if game is playing
    if game.is_playing:
        #launch a game
        game.update(screen)

    #check if game not playing
    else:
        #add main page
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)







    #update screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
            pygame.quit()
            print("Fermeture du jeu")

        #detect if the player is releasing a key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detect if E is pressed (projectile)
            if event.key == pygame.K_e:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check if button is clicked
            if play_button_rect.collidepoint(event.pos):
                #lauch the game
                game.start()
                #lauch sound
                game.sound_manager.play("click")
    #choose nb of fps
    clock.tick(FPS)


#while running is True, the game is launched

"""
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
    player.jump()
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

"""