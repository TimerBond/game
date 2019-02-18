import pygame
import RenderMap as renderMap
from const import *
import Background as bg
import Clouds as cloud
import Coin as coin
import Monster as monster
import random
import sys
import Money as money


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Runner"]
    fon = pygame.transform.scale(pygame.image.load('sprites/fon.png'), (SIZE[0], SIZE[1]))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 200)
    text_coord = 450
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = text_coord
        intro_rect.x = 475
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


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
            elif map[y][x] == 'M':
                monster.Monster(monsters, type_monster[2], x, y)
            elif map[y][x] == 'C':
                money.Money(coin_sprites, x, y)
    return x, y


pygame.font.init()
moneyFont = pygame.font.SysFont('Money Shower', 50)
moneyIcon = moneyFont.render("0", False, (0, 0, 0))
all_sprites = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()
back = pygame.sprite.Group()
clouds_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()

type_monster = {
    1: "sprites/monster.png",
    2: "sprites/monster1.png",
    3: "sprites/monster2.png"
}
c = coin.Coin(coin_sprites)

width, height = generate_map(load_level("map_1.txt"))

screen = pygame.display.set_mode(SIZE)
background = bg.Background(back)
for _ in range(5):
    cl = cloud.Cloud(clouds_sprites)
running = True

start_screen()
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
    screen.blit(moneyIcon, (1300, 10))
    monsters.draw(screen)
    pygame.display.flip()
