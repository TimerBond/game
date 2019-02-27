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
import HeroBullet
import Heart
import Finish


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
                Monster.Monster(monsters, type_monster["1_1"], x, y, all_blocks, bullets, all_sprites, player_group,
                                hero_bullets)
            elif map[y][x] == 'C':
                money.Money(coin_sprites, x, y, all_sprites, player_group)
                count += 1
            elif map[y][x] == 'P':
                global player_x, player_y
                player_x = x * CELL_SIZE
                player_y = y * CELL_SIZE
            elif map[y][x] == 'F':
                Finish.Finish(finish_group, x, y)
    return x, y, count


def Camera(all_sprites):
    for sprite in all_sprites:
        sprite.rect.x -= PLAYER_SPEED


pygame.font.init()
moneyFont = pygame.font.SysFont('Money Shower', 50)
lifeFont = pygame.font.SysFont('Life Shower', 50)
all_sprites = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()
back = pygame.sprite.Group()
clouds_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()
bullets = pygame.sprite.Group()
hero_bullets = pygame.sprite.Group()
finish_group = pygame.sprite.Group()
heart = pygame.sprite.Group()
h = Heart.Heart(heart)

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

player = MainPlayer.AnimatedSprite(player_x, player_y, player_group, all_blocks)
go = False
clock = pygame.time.Clock()
player_HP = 3
while running:
    player_HP = player.HP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 114:
                player.changeHeightMode(1)
            if event.key == 116:
                player.changeHeightMode(0)
            if event.key == 275:
                go = player.forward()
                Camera(all_sprites)
            if event.key == 32:
                if go:
                    player.jump()
            if event.key == 118:
                pos_x = player.rect.x
                pos_y = player.rect.y
                HeroBullet.HeroBullet(hero_bullets, all_sprites, pos_x, pos_y, all_blocks, monsters)
        elif event.type == pygame.KEYUP:
            if event.key == 275:
                go = False
                player.stop()
    if go:
        go = player.forward()
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
    hero_bullets.draw(screen)
    hero_bullets.update()
    monsters.draw(screen)
    monsters.update()
    bullets.draw(screen)
    bullets.update()
    player_group.draw(screen)
    player_group.update()
    heart.draw(screen)
    lifeIcon = lifeFont.render(str(player_HP), False, (0, 0, 0))
    screen.blit(lifeIcon, (50, 5))
    finish_group.draw(screen)
    clock.tick(10)
    pygame.display.flip()
