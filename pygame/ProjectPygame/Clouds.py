import pygame
import random


class Cloud(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/cloud.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Cloud.image
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, 300)
        self.rect.x = random.randint(0, 1100)
        self.group = group

    def update(self, *args):
        if len(pygame.sprite.spritecollide(self, self.group, False)) > 1:
            self.rect.x = random.randint(0, 1100)
            self.rect.y = random.randint(0, 300)
        self.rect.x -= 5
        if self.rect.x + self.rect.w < 0:
            self.rect.x = 1300
