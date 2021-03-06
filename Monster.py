import pygame
from Projectile import Projectile
import random
import animation
import math

# class Player
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 20
        self.velocity = random.randint(1,2)

        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1280 + random.randint(0,300)
        self.rect.y = 300 + random.randint(-200,200)
        self.start_animation()
        self.y0 = self.rect.y


    def damage(self, amount):
        #give damage
        self.health -= amount

        #check if monster died
        if self.health <= 0:
            self.game.all_monsters.remove(self)

    def update_animations(self):
        self.animate(loop = True)


    def update_health_bar(self, surface):#draw health bar
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health * 20, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x+10, self.rect.y-20, self.health*20, 5])


    def update_speed(self):
        self.velocity += self.game.score//1000

    def forward(self):
        self.rect.x -= self.velocity
        self.rect.y = 100*math.cos(self.rect.x/222) + self.y0
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)

        if self.rect.x <= -10:
            self.game.all_monsters.remove(self)

        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(1)


