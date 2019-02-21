import pygame


class Bullet(pygame.sprite.Sprite):
    image = pygame.image.load("sprites/fireball_1.png")


    def __init__(self, group, x, y, direction):
        super().__init__(group)
        self.image = Bullet.image
        self.rect = self.image.get_rect().move(
            x - 10, y
        )
        self.direction = direction
        self.type = {
            0: -5,
            1: 5
        }

    def update(self, *args):
        self.rect.x += self.type[self.direction]
