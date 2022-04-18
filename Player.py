import Objects as obj
import Ecosystem as eco
import Monster as mt
import time

g = 9.81

class Player(obj.Objects):
    def __init__(self, life, x, y, eco):

        """Le constructeur de la classe Player.
        x, y : int
        """
        super().__init__(x, y, eco)
        self.life = life
        self.time_in_air = 0
        self.spdy = 0

    def jump(self):
        """
        La fonction qui fait sauter le joueur avec un mouvement proche de la physique réelle

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """
        if "je click sur la touche" and not(self.on_floor()):
            t = time.time() - self.time_in_air
            self.y = -0.5*g*t**2 + self.spdy*t + self.y


    def on_floor(self):
        """
        La fonction qui teste si le joueur est au sol

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """
        if self.x == "à définir":
            return True
        return False

    def attack(self):
        """
        La fonction qui fait tirer le joueur

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """
        if "je click sur la souris":
            "créer une attaque"
