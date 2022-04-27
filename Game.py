from Player import Player
from Monster import Monster
import pygame

#class Game
from info_jetpack.Sounds import SoundManager


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
        self.pressed = {}
        #setup sound
        self.sound_manager = SoundManager()
        #put score to zero
        self.score = 0

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        #put the game to zero
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        #play the sound
        self.sound_manager.play("game_over")


    def update(self, screen):


        #set score
        font = pygame.font.SysFont("SANSATION", 25)
        score_text = font.render(f"SCORE : {self.score}", 1, (255,255,255))
        screen.blit(score_text, (20, 20))
        # apply player image
        screen.blit(self.player.image, self.player.rect)

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

        # get player projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # get player projectiles
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animations()
        # check if go down or up
        if self.pressed.get(pygame.K_SPACE) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < screen.get_height() - 200:
            self.player.move_down()





