import pygame
from const import *


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, all_sprites, player_HP, all_blocks):
        super().__init__(all_sprites)
        self.frames = []
        self.all_blocks = all_blocks
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(
            x, y - self.rect.h + CELL_SIZE + 3
        )
        self.HP = player_HP

    def cut_sheet(self, sheet, columns, rows):

        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.y += 10
        if pygame.sprite.spritecollideany(self, self.all_blocks):
            self.rect.y -= 10
