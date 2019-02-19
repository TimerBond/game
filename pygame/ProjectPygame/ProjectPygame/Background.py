import pygame


class Background(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/background.png")

    def __init__(self, back):
        super().__init__(back)
        self.image = Background.image
        self.rect = self.image.get_rect().move(0, 0)
