import pygame
import random

# 初始化Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("打飞机游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 游戏时
clock = pygame.time.Clock()
fps = 60

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top > screen_height + 10 or self.rect.left < -25 or self.rect.right > screen_width + 20:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# 创建精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 创建玩家飞机
player = Player()
all_sprites.add(player)

# 创建敌机
for i in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏循环
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # 更新精灵
    all_sprites.update()

    # 检查子弹与敌机的碰撞
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # 检查玩家与敌机的碰撞
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # 绘制屏幕
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()