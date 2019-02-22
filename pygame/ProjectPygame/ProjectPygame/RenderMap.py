import pygame
from const import *


class Block(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/block.png")

    def __init__(self, pos_x, pos_y, *d):
        super().__init__(*d)
        self.image = Block.image
        self.rect = self.image.get_rect().move(
            CELL_SIZE * pos_x, CELL_SIZE * pos_y
        )
