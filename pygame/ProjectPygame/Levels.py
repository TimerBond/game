import os, pygame


class Level(pygame.sprite.Sprite):
    def __init__(self, group, map, x, y, level):
        super().__init__(group)
        self.image = map
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = level

    def get_map(self, map):
        return os.listdir('maps')[map]

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.get_map(self.level)
