import pygame
from const import *


class Coin(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/coin.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Coin.image
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = 5
