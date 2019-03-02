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
import Menu


pygame.init()
def terminate():
    pygame.quit()
    sys.exit()


def start_screen(fon):
    intro_text = []
    if fon != "sprites/gameover.png" and fon != "sprites/win.png":
        intro_text.append("Runner")
    fon = pygame.transform.scale(pygame.image.load(fon), (SIZE[0], SIZE[1]))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 200)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = text_coord
        intro_rect.x = 450
        screen.blit(string_rendered, intro_rect)
    menu = Menu.Menu(SIZE[1] // 3, SIZE[0] // 3)
    screen.blit(menu.image, (SIZE[0] // 3, SIZE[1] // 3))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                y = menu.get_click(event.pos)
                if y is None:
                    pass
                elif y <= len(MAPS) - 1:
                    global mapName
                    mapName = MAPS[y]
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
                Finish.Finish(finish_group, x, y, all_sprites)
    return x, y, count


def Camera(all_sprites, to):
    for sprite in all_sprites:
        sprite.rect.x -= PLAYER_SPEED * to


screen = pygame.display.set_mode(SIZE)
pygame.font.init()
moneyFont = pygame.font.SysFont('Money Shower', 50)
lifeFont = pygame.font.SysFont('Life Shower', 50)
play = True
dead = False
finish = False
while play:
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
    Heart.Heart(heart)

    player_group = pygame.sprite.Group()
    type_monster = {
        "1_1": "sprites/monster1_1.png",
        "1_2": "sprites/monster1_2.png"
    }
    coin.Coin(coin_sprites)
    player_x = 0
    player_y = 0

    background = bg.Background(back)
    for _ in range(5):
        cl = cloud.Cloud(clouds_sprites, all_sprites)
    running = True

    mapName = ""
    if dead:
        start_screen('sprites/gameover.png')
    elif finish:
        start_screen('sprites/win.png')
    else:
        start_screen('sprites/fon.png')

    finish = False
    dead = False

    width, height, count_coins = generate_map(load_level(mapName))
    player = MainPlayer.AnimatedSprite(player_x, player_y, player_group, all_blocks, all_sprites, finish_group)
    #pygame.mixer.music.load('sounds/C418 - Subwoofer Lullaby.mp3')
    #pygame.mixer.music.play()
    go = False
    clock = pygame.time.Clock()
    runned = 0
    player_HP = 3
    to = 1
    while running:
        player_HP = player.HP
        if player_HP == 0:
            dead = True
            break
        elif player.isFinished:
            finish = True
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 276:
                    to = -1
                    go = player.forward(to)
                    Camera(all_sprites, to)
                if event.key == 114:
                    player.changeHeightMode(1)
                if event.key == 116:
                    player.changeHeightMode(0)
                if event.key == 275:
                    to = 1
                    go = player.forward(to)
                    Camera(all_sprites, to)
                if event.key == 32:
                    if go and player.heightMode == 0:
                        player.jump()
                if event.key == 118:
                    pos_x = player.rect.x
                    pos_y = player.rect.y
                    HeroBullet.HeroBullet(hero_bullets, all_sprites, pos_x, pos_y, all_blocks, monsters, bullets, to)
            elif event.type == pygame.KEYUP:
                if event.key == 273:
                    pygame.mixer.music.set_volume(1)
                elif event.key == 274:
                    pygame.mixer.music.set_volume(0.5)
                elif event.key == 275 or event.key == 276:
                    go = False
                    player.stop()
        if not play:
            break
        if runned < 0:
            go = False
        if go:
            go = player.forward(to)
            if width * CELL_SIZE - SIZE[0] > runned:
                Camera(all_sprites, to)
            runned += PLAYER_SPEED * to
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
