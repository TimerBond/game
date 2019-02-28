import pygame
from const import *


class Bullet(pygame.sprite.Sprite):

    def __init__(self, group, x, y, direction, all_blocks, all_sprites, player):
        super().__init__(group, all_sprites)
        self.group = group
        self.direction = direction
        self.player = player
        if self.direction == 0:
            self.image = pygame.image.load("sprites/fireball_1.png")
        else:
            self.image = pygame.image.load("sprites/fireball_2.png")
        self.rect = self.image.get_rect().move(
            x, y + 20
        )
        self.type = {
            0: -10,
            1: 10
        }
        self.all_blocks = all_blocks
        self.catch = 0

    def update(self, *args):
        self.rect.x += self.type[self.direction]
        if pygame.sprite.spritecollideany(self, self.all_blocks) or self.rect.x < 0:
            self.group.remove(self)
        if pygame.sprite.spritecollideany(self, self.player):
            pygame.mixer.music.load('sounds/Звук урона в майнкрафт.mp3')
            pygame.mixer.music.play()
            self.group.remove(self)
            for i in self.player:
                i.HP -= 1
