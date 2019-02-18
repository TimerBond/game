import pygame
from const import *


class Money(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/coin.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Money.image
        self.rect = self.image.get_rect().move(
            CELL_SIZE * x, CELL_SIZE * y
        )
