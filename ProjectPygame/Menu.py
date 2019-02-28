import pygame
from const import *


class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = self.draw()

    def draw(self):
        surf = pygame.Surface((450, 400))
        surf.fill((255, 255, 255))
        h = 400 // len(MAPS)
        y = 0
        pygame.font.init()
        nameMap = pygame.font.SysFont('Map', 50)
        for i in range(len(MAPS)):
            pygame.draw.rect(surf, (255, 255, 255), (0, y, 450, h))
            name = nameMap.render(MAPS[i], False, (0, 0, 0))
            surf.blit(name, (150, y + h // 2))
            y += h
        return surf

