import pygame
from const import *


class Finish(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.image.load('sprites/finish.png')
        self.rect = self.image.get_rect()
        self.rect.x = x * CELL_SIZE
        self.rect.y = y * CELL_SIZE
