import pygame
from const import *
import Bullet


class Monster(pygame.sprite.Sprite):

    def __init__(self, group, type, x, y, blocks, bullets, all_sprites):
        super().__init__(group, all_sprites)
        self.image = pygame.image.load(type)
        self.all_sprites = all_sprites
        self.rect = self.image.get_rect().move(
            CELL_SIZE * x - 5, CELL_SIZE * y - 5
        )
        self.type = {
            0: -2,
            1: 2
        }
        self.direct = 0
        self.blocks = blocks
        self.bullets = bullets
        self.timeToShoot = 1

    def update(self, *args):
        if 0 <= self.rect.x <= 1300 and self.timeToShoot % 60 == 0:
            Bullet.Bullet(self.bullets, self.rect.x, self.rect.y, self.direct, self.blocks, self.all_sprites)
        self.timeToShoot += 1
        if self.direct == 0 and self.rect.x <= 1300:
            pass
        self.rect.x += self.type[self.direct] * 25
        self.rect.y += 5
        block = pygame.sprite.spritecollide(self, self.blocks, False)
        if len(block) == 0:
            self.rect.y -= 5
            self.rect.x -= self.type[self.direct] * 25
            if self.direct == 0:
                self.image = pygame.image.load("sprites/monster1_2.png")
            else:
                self.image = pygame.image.load("sprites/monster1_1.png")
            self.direct = abs(self.direct - 1)
        else:
            self.rect.y -= 5
            self.rect.x -= self.type[self.direct] * 25
            self.rect.x += self.type[self.direct]
            block = pygame.sprite.spritecollide(self, self.blocks, False)
            if len(block) != 0:
                if self.direct == 0:
                    self.image = pygame.image.load("sprites/monster1_2.png")
                else:
                    self.image = pygame.image.load("sprites/monster1_1.png")
                self.direct = abs(self.direct - 1)
