import Objects as obj
import Ecosystem as eco
import Player as pl
import time
import numpy as np
g = 9.81


class Monster(Object):
    def __init__(self, life, x, y, eco):

        """Le constructeur de la classe Player.
        x, y : int
        """
        super().__init__(x, y, eco)
        self.life = life
        self.time_in_air = 0
        self.spdy = 0
        self.t0 = time.time()

    def move(self):
        """
        La fonction qui fait se déplacer le monstre avec un mouvement proche de la physique réelle

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """

        t = time.time() - self.t0
        self.y = 200*np.cos(t)
        self.x -= self.spdx

