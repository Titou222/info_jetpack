import pygame
from Projectile import Projectile
import animation

# class Player
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 500

    def launch_projectile(self):
        #create a projectile
        self.all_projectiles.add(Projectile(self))
        #launch the animation
        self.start_animation()
        #launch sound
        self.game.sound_manager.play("tir")
    def update_health_bar(self, surface):
        #draw health bar
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 50, self.rect.y + 20, self.max_health * 25, 10])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x+50, self.rect.y + 20, self.health*25, 10])

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= 1
        else :
            #if player is dying
            self.game.game_over()

    def update_animation(self):
        self.animate()







# import Objects as obj
# import Ecosystem as eco
# import Monster as mt
# import time
#
# g = 9.81
#
# class Player(obj):
#     def __init__(self, life, x, y, eco):
#         """
#         Le constructeur de la classe Player.
#         x, y : int
#         """
#         super().__init__(x, y, eco)
#         self.life = life
#         self.time_in_air = 0
#         self.spdy = 0
#
#     def jump(self):
#         """
#         La fonction qui fait sauter le joueur avec un mouvement proche de la physique réelle
#
#         Paramètres
#         ----------
#         Rien
#
#         Renvoie
#         -------
#         Rien
#         """
#         if "je click sur la touche" and not(self.on_floor()):
#             t = time.time() - self.time_in_air
#             self.y = -0.5*g*t**2 + self.spdy*t + self.y
#
#
#     def on_floor(self):
#         """
#         La fonction qui teste si le joueur est au sol
#
#         Paramètres
#         ----------
#         Rien
#
#         Renvoie
#         -------
#         Rien
#         """
#         if self.x == "à définir":
#             return True
#         return False
#
#     def attack(self):
#         """
#         La fonction qui fait tirer le joueur
#
#         Paramètres
#         ----------
#         Rien
#
#         Renvoie
#         -------
#         Rien
#         """
#         if "je click sur la souris":
#             "créer une attaque"
