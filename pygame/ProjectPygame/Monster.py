import pygame
from const import *


class Monster(pygame.sprite.Sprite):

    def __init__(self, group, type, x, y):
        super().__init__(group)
        self.image = pygame.image.load(type)
        self.rect = self.image.get_rect().move(
            CELL_SIZE * x, CELL_SIZE * y
        )
