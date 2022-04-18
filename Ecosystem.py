import Objects as obj
import time
import Player as pl
import Ecosystem as eco

class Ecosystem:

    def __init__(self, sizex, sizey,eco):
        """
        Le constructeur de la classe Ecosystem

        Paramètres
        ----------
        sizex : int
        sizey : int
        eco : Ecosystem

        Renvoie
        -------
        Rien
        """
        self.list_obj = ["à définir"]
        self.sizex, self.sizey = sizex, sizey
        self.image = "à définir"
        self.time = time.time()
        self.distance = 0
        self.score = 0
        self.background_spd = "à définir"
        self.backgroundx = 0
        self.backgroundy = 0


    def update_score(self):
        """
        La fonction qui actualise le score

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """
        self.score = self.time

    def update_background(self):
        """
        La fonction qui actualise le déplacement du fond d'écran

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """
        self.backgroundx += self.background_spd

if __name__ == "__main__":

    eco = Ecosystem(720,1080)
    while pl.life > 0:
        eco.update_score()
        eco.update_background()
