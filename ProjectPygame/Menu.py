import pygame
from const import *


class Menu(pygame.sprite.Sprite):

    def __init__(self, top, left):
        super().__init__()
        self.image = self.draw()
        self.top = top
        self.left = left

    def draw(self):
        self.height = len(MAPS)
        surf = pygame.Surface((450, 100 * len(MAPS)))
        surf.fill((255, 255, 255))
        self.h = 100
        y = 0
        pygame.font.init()
        nameMap = pygame.font.SysFont('Map', 50)
        for i in range(len(MAPS)):
            pygame.draw.rect(surf, (255, 255, 255), (0, y, 450, self.h))
            name = nameMap.render(MAPS[i], False, (0, 0, 0))
            surf.blit(name, (150, y + self.h // 2))
            y += self.h
        return surf

    def get_cell(self, mouse_pos):
        x = mouse_pos[0] // 450
        y = mouse_pos[1] // self.h
        if x > 1 or y > self.height - 1:
            return None
        else:
            return y

    def get_click(self, mouse_pos):
        cell = self.get_cell((mouse_pos[0] - self.left, mouse_pos[1] - self.top))
        return cell
