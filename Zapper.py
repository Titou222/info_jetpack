import pygame
import random

import pygame
from Projectile import Projectile
import random
import animation
import math

# class Player
class Zapper(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 20
        self.velocity = random.randint(1,4) +0.00001*self.game.score

        self.image = pygame.image.load("assets/Zapper_h.png")
        self.image = pygame.transform.scale(self.image,self.HorV())
        self.rect = self.image.get_rect()
        self.rect.x = 1280 + random.randint(0,300)
        self.rect.y = 300 + random.randint(-200,200)
        self.y0 = self.rect.y

    def HorV(self):
        a=0
        if random.randint(0,1) == 0:
            a = (random.randint(200,400),60)
        else:
            a = ( 60,random.randint(200, 400))
        return a

    def damage(self, amount):
        #give damage
        self.health -= amount

        #check if monster died
        if self.health <= 0:
            self.game.all_zapper.remove(self)



    def forward(self):
        self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)

        if self.rect.x <= -350:
            self.game.all_zapper.remove(self)

        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(1)


