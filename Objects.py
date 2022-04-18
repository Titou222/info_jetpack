import Ecosystem as eco

class Object:

    def __init__(self, life, x, y):
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


