import pygame
from const import *


class HeroBullet(pygame.sprite.Sprite):

    def __init__(self, group, all_sprites, x, y, all_blocks, monsters, bullets, to):
        super().__init__(group, all_sprites)
        self.group = group
        self.bullets = bullets
        self.to = to
        if self.to == 1:
            self.image = pygame.image.load("sprites/heroBullet_1.png")
        else:
            self.image = pygame.image.load("sprites/heroBullet_2.png")
        self.rect = self.image.get_rect().move(
            x, y + 35
        )
        self.all_blocks = all_blocks
        self.monsters = monsters

    def update(self, *args):
        self.rect.x += 10 * self.to
        if pygame.sprite.spritecollideany(self, self.all_blocks):
            self.group.remove(self)
        bullets = pygame.sprite.spritecollide(self, self.bullets, False)
        if len(bullets) > 0:
            self.group.remove(self)
            for i in bullets:
                self.bullets.remove(i)
