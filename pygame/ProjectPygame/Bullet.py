import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, group, x, y, direction, all_blocks, all_sprites):
        super().__init__(group, all_sprites)
        self.group = group
        self.direction = direction
        if self.direction == 0:
            self.image = pygame.image.load("sprites/fireball_1.png")
        else:
            self.image = pygame.image.load("sprites/fireball_2.png")
        self.rect = self.image.get_rect().move(
            x, y + 20
        )
        self.type = {
            0: -10,
            1: 10
        }
        self.all_blocks = all_blocks

    def update(self, *args):
        self.rect.x += self.type[self.direction]
        if pygame.sprite.spritecollideany(self, self.all_blocks) or self.rect.x < 0:
            self.group.remove(self)
