import pygame
from const import *


class AnimatedSprite(pygame.sprite.Sprite):
    modes = {
        0: (pygame.image.load('sprites/anim1.png'), pygame.image.load('sprites/anim1_1.png'), 8, 1),
        1: (pygame.image.load('sprites/anim2.png'), pygame.image.load('sprites/anim2_2.png'), 9, 1),
        2: (pygame.image.load('sprites/anim3.png'), pygame.image.load('sprites/anim3_3.png'), 7, 1),
        3: (pygame.image.load('sprites/anim4.png'), pygame.image.load('sprites/anim4_4.png'), 9, 1)
    }

    def __init__(self, x, y, group, all_blocks, all_sprites):
        super().__init__(group, all_sprites)
        self.heightMode = 0
        self.mode = 0
        self.frames = []
        self.cur_frame = 0
        self.all_blocks = all_blocks
        self.HP = 3
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.changeMode(0)
        self.image = self.frames[self.cur_frame]
        self.rect.x = x
        self.rect.y = y - self.rect.h + CELL_SIZE + 5

    def cut_sheet(self, sheet, columns, rows):
        self.rect.h = sheet.get_height() // rows
        self.rect.w = sheet.get_width() // columns
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.y += 50
        blocks = pygame.sprite.spritecollide(self, self.all_blocks, False)
        if len(blocks) > 0:
            self.rect.y -= 50
            self.rect.y = blocks[0].rect.y - self.rect.h + 5

    def changeMode(self, mode):
        self.frames = []
        self.cut_sheet(AnimatedSprite.modes[mode][self.heightMode], AnimatedSprite.modes[mode][2], AnimatedSprite.modes[mode][3])
        self.mode = mode

    def forward(self, to):
        if self.mode == 0:
            if to == 1:
                self.changeMode(1)
            else:
                self.changeMode(3)
        self.rect.x += PLAYER_SPEED * to
        blocks = pygame.sprite.spritecollide(self, self.all_blocks, False)
        for block in blocks:
            if block.rect.y < self.rect.y + self.rect.h - 10:
                self.rect.x -= PLAYER_SPEED * to
                return False
        return True

    def stop(self):
        self.changeMode(0)

    def jump(self):
        mode = self.mode
        self.changeMode(2)
        if self.heightMode == 0:
            self.rect.y -= CELL_SIZE
            self.rect.x += CELL_SIZE // 2
        self.changeMode(mode)

    def changeHeightMode(self, newMode):
        self.heightMode = newMode
        if newMode == 1:
            self.rect.y += CELL_SIZE // 2
        else:
            self.rect.y -= CELL_SIZE // 2
        self.changeMode(self.mode)



