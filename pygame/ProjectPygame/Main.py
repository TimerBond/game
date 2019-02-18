import pygame
import RenderMap as renderMap
from const import *
import Background as bg
import Clouds as cloud
import Coin as coin


def load_level(filename):
    filename = "maps/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def generate_map(map):
    y, x = None, None
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '#':
                renderMap.Block(x, y, all_blocks, all_sprites)
    return x, y


pygame.font.init()
moneyFont = pygame.font.SysFont('Money Shower', 50)
money = moneyFont.render("0", False, (0, 0, 0))
all_sprites = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()
back = pygame.sprite.Group()
clouds_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

c = coin.Coin(coin_sprites)

width, height = generate_map(load_level("map_1.txt"))

screen = pygame.display.set_mode(SIZE)
background = bg.Background(back)
for _ in range(5):
    cl = cloud.Cloud(clouds_sprites)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    back.draw(screen)
    clouds_sprites.draw(screen)
    clouds_sprites.update()
    all_blocks.draw(screen)
    coin_sprites.draw(screen)
    screen.blit(money, (1300, 10))
    pygame.display.flip()
