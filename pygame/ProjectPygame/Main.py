import pygame
import RenderMap as renderMap
from const import *
import Background as bg
import Clouds as cloud
import Coin as coin
import Monster
import sys
import Money as money
import MainPlayer


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
    count = 0
    y, x = None, None
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '#':
                renderMap.Block(x, y, all_blocks, all_sprites)
            elif map[y][x] == 'M':
                Monster.Monster(monsters, type_monster["1_1"], x, y, all_blocks, bullets, all_sprites)
            elif map[y][x] == 'C':
                money.Money(coin_sprites, x, y, all_sprites, player_group)
                count += 1
            elif map[y][x] == 'P':
                global player_x, player_y
                player_x = x * CELL_SIZE
                player_y = y * CELL_SIZE
    return x, y, count


def Camera(all_sprites):
    for sprite in all_sprites:
        sprite.rect.x -= PLAYER_SPEED


pygame.font.init()
moneyFont = pygame.font.SysFont('Money Shower', 50)
all_sprites = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()
back = pygame.sprite.Group()
clouds_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player_group = pygame.sprite.Group()
type_monster = {
    "1_1": "sprites/monster1_1.png",
    "1_2": "sprites/monster1_2.png"
}
c = coin.Coin(coin_sprites)
player_x = 0
player_y = 0

width, height, count_coins = generate_map(load_level("map_1.txt"))

screen = pygame.display.set_mode(SIZE)
background = bg.Background(back)
for _ in range(5):
    cl = cloud.Cloud(clouds_sprites, all_sprites)
running = True

start_screen()

player = MainPlayer.AnimatedSprite(pygame.image.load('sprites/anim1.png'),
                                   8, 1, player_x, player_y, player_group)
was = False
b = False
t = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 275:
                player_group.empty()
                player = MainPlayer.AnimatedSprite(pygame.image.load('sprites/anim2.png'),
                                                   9, 1, player_x, player_y, player_group)
                was = True
            if event.key == 32:
                player_group.empty()
                player = MainPlayer.AnimatedSprite(pygame.image.load('sprites/anim3.png'),
                                                   7, 1, player_x, player_y, player_group)
                b = True
        elif event.type == pygame.KEYUP:
            if event.key == 275:
                player_group.empty()
                player = MainPlayer.AnimatedSprite(pygame.image.load('sprites/anim1.png'),
                                                   8, 1, player_x, player_y, player_group)
                was = False
    if b:
        t += 1
    if t == 7:
        b = False
        t = 0
        player_group.empty()
        player = MainPlayer.AnimatedSprite(pygame.image.load('sprites/anim1.png'), 8, 1, 0, 0, player_group)
    if was:
        Camera(all_sprites)
    screen.fill((255, 255, 255))
    back.draw(screen)
    clouds_sprites.draw(screen)
    clouds_sprites.update()
    all_blocks.draw(screen)
    coin_sprites.draw(screen)
    coin_sprites.update()
    moneyIcon = moneyFont.render(str(count_coins - len(coin_sprites) + 1), False, (0, 0, 0))
    screen.blit(moneyIcon, (1300, 10))
    monsters.draw(screen)
    monsters.update()
    bullets.draw(screen)
    bullets.update()
    player_group.draw(screen)
    player_group.update()
    clock.tick(10)
    pygame.display.flip()
