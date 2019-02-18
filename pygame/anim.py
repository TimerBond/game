import os, pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        print(self.frames)

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


pygame.init()
size = width, height = 360, 120
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
move = AnimatedSprite(load_image('anim1.png'), 8, 1, 0, 0)
clock = pygame.time.Clock()
t = 0
b = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            all_sprites.empty()
            move = AnimatedSprite(load_image('anim1.png'), 8, 1, 0, 0)
            b = False
        if event.type == pygame.KEYDOWN:
            all_sprites.empty()
            if event.key == 275:
                move = AnimatedSprite(load_image('anim2.png'), 9, 1, 0, 0)
                print('run')
            if event.key == 32:
                move = AnimatedSprite(load_image('anim3.png'), 7, 1, 0, 0)
                b = True
                print('jump')
    screen.fill(pygame.Color('white'))
    if b:
        t += 1
    if t == 7:
        t = 0
        b = False
        all_sprites.empty()
        move = AnimatedSprite(load_image('anim1.png'), 8, 1, 0, 0)
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
