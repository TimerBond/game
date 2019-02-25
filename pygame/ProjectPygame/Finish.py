import pygame


class Finish(pygame.sprite.Sprite):
    image = pygame.image.load('sprites/finish.png')

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Finish.image
        self.rect = self.image.get_rect().move(
            x, y
        )
