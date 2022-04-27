import pygame
from Projectile import Projectile
import random
import animation

# class Player
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.velocity = 5 + random.randint(0,2)

        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1280 + random.randint(0,300)
        self.rect.y = 300 + random.randint(-200,200)
        self.start_animation()

    def damage(self, amount):
        #give damage
        self.health -= amount

        #check if monster died
        if self.health <= 0:

            #respawn as other mob
            self.rect.x =  1280 + random.randint(0,300)
            self.rect.y = 300 + random.randint(-200, 200)
            self.velocity = 5 + random.randint(0,2)
            self.health = self.max_health

    def update_animations(self):
        self.animate(loop = True)


    def update_health_bar(self, surface):#draw health bar
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health * 20, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x+10, self.rect.y-20, self.health*20, 5])



    def forward(self):
        self.rect.x -= self.velocity

        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)

        if self.rect.x <= -10:
            self.rect.x = 1280



