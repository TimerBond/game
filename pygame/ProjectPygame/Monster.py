import pygame
from const import *


class Monster(pygame.sprite.Sprite):

    def __init__(self, group, type, x, y, blocks):
        super().__init__(group)
        self.image = pygame.image.load(type)
        self.rect = self.image.get_rect().move(
            CELL_SIZE * x - 5, CELL_SIZE * y - 5
        )
        self.type = {
            0: -2,
            1: 2
        }
        self.direct = 0
        self.blocks = blocks

    def update(self, *args):
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
