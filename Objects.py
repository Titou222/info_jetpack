
import time
import numpy as np

class Object:

    def __init__(self, life, x, y,app):
        """
        Le constructeur de la classe Object

        Paramètres
        ----------
        life, x, y

        Renvoie
        -------
        Rien
        """

        self.life = life
        self.x, self.y = x,y
        self.app = app

    def colision(self, obj):
        """
        La fonction qui teste la colision entre les hitboxs de deux objets

        Paramètres
        ----------
        obj :

        Renvoie
        -------
        True : s'il y a colision
        False : sinon
        """

        if """les hitbox se touchent""":
            return True
        return False

    def hit(self):
        """
        La fonction qui fait perdre un point de vie s'il y a colision entre le joueur et un monstre

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """

        #attention il y aura peut-être un problème avec cette façon de dire, par exemple si le joueur et un monstre se touchent
        #il se peut que les deux soient considérés comme touchés ou non, et dans ce cas la vie sera peut-être différente de ce qu'on veut

        for e in eco.list_obj:
            if self.colision(e):
                self.life -= 1

    def mort(self):
        """
        La fonction qui fait disparaitre un objet s'il n'a plus de vie

        Paramètres
        ----------
        Rien

        Renvoie
        -------
        Rien
        """

        for e in eco.list_obj:
            if e.life <=0 :
                eco.list_obj.remove(e)


class Player(Object):
    def __init__(self, life, x, y, app):

        """Le constructeur de la classe Player.
        x, y : int
        """
        super().__init__(life, x, y, app)
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

class Monster(Object):
    def __init__(self, life, x, y, app):

        """Le constructeur de la classe Player.
        x, y : int
        """
        super().__init__(x, y, app)
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
