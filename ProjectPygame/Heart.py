import pygame


class Heart(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/heart.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Heart.image
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 5
