import pygame
from const import *


class Finish(pygame.sprite.Sprite):

    def __init__(self, group, x, y, all_sprites):
        super().__init__(group, all_sprites)
        self.image = pygame.image.load('sprites/finish.png')
        self.rect = self.image.get_rect().move(
            x * CELL_SIZE, y * CELL_SIZE
        )
