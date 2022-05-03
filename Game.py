from Player import Player
from Monster import Monster
import pygame
import random
from Zapper import Zapper

#class Game
from Sounds import SoundManager


class Game:

    def __init__(self):
        #define if game is played
        self.is_playing = False
        #generate our player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.all_zapper = pygame.sprite.Group()
        self.pressed = {}
        #setup sound
        self.sound_manager = SoundManager()
        #put score to zero
        self.score = 0
        self.counter = 1
        self.name = ""

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_zapper()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_zapper(self):
        zapper = Zapper(self)
        self.all_zapper.add(zapper)

    def zapper_spawning(self):
        c = 0
        if self.score%1000 == 0:
                    self.spawn_zapper()

    def monster_spawning(self):
        if self.score%800 == 0 :
            self.counter +=1
            for j in range(self.counter//4 + random.randint(-self.score//100, +self.score//100)):
                self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        #put the game to zero
        self.all_monsters = pygame.sprite.Group()
        self.all_zapper = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        #play the sound
        self.sound_manager.play("game_over")

    def update_main(self,screen):
        # display text
        font = pygame.font.SysFont("SANSATION", 25)
        name_text = font.render(f"Name : {self.name}", 1, (255, 255, 255))
        screen.blit(name_text, (500, 350))

    def update(self, screen):


        #set score
        font = pygame.font.SysFont("SANSATION", 25)
        score_text = font.render(f"SCORE : {self.score}", 1, (255,255,255))
        screen.blit(score_text, (20, 20))
        # apply player image
        screen.blit(self.player.image, self.player.rect)

        # spawn monsters
        self.monster_spawning()
        self.zapper_spawning()
        # update score
        self.score += 1
        # update health bar of player
        self.player.update_health_bar(screen)

        #update player animation
        self.player.update_animation()

        # apply the set of projectile
        self.player.all_projectiles.draw(screen)

        # apply the set of monsters
        self.all_monsters.draw(screen)
        self.all_zapper.draw(screen)

        # get player projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # get player projectiles
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animations()
            monster.update_speed()
        for zapper in self.all_zapper:
            zapper.forward()

        # check if go down or up
        if self.pressed.get(pygame.K_SPACE) and self.player.rect.y > 50:
            self.player.j +=1
            self.player.f = 0
            self.player.jump()

        elif not self.pressed.get(pygame.K_SPACE) and self.player.rect.y < 550:
            self.player.f += 1
            self.player.j  = 0
            self.player.fall()






