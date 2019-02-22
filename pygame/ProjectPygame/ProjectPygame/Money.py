import pygame
from const import *


class Money(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/coin.png")

    def __init__(self, group, x, y, all_sprires, player):
        super().__init__(group, all_sprires)
        self.image = Money.image
        self.group = group
        self.rect = self.image.get_rect().move(
            CELL_SIZE * x, CELL_SIZE * y
        )
        self.player = player

    def update(self, *args):
        if pygame.sprite.spritecollideany(self, self.player):
            self.group.remove(self)
