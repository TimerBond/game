import pygame
from const import *


class Coin(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/coin.png")

    def __init__(self, group, player):
        super().__init__(group)
        self.group = group
        self.image = Coin.image
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = 5
        self.player = player

    def update(self, *args):
        if pygame.sprite.spritecollideany(self, self.player):
            increaseCoins()
            self.group.remove(self)

