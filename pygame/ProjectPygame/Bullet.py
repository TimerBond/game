import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, group, x, y, direction):
        super().__init__(group)
        self.direction = direction
        if self.direction == 0:
            self.image = pygame.image.load("sprites/fireball_1.png")
        else:
            self.image = pygame.image.load("sprites/fireball_2.png")
        self.rect = self.image.get_rect().move(
            x - 10, y
        )
        self.type = {
            0: -5,
            1: 5
        }

    def update(self, *args):
        self.rect.x += self.type[self.direction]
