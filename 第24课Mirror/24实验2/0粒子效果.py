import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸和背景色
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("下雨效果")

# 定义雨滴粒子的属性
raindrops = []
for _ in range(20):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    speed = random.randint(5, 15)
    raindrops.append([x, y, speed])

# 设置雨滴颜色
raindrop_color = (0, 0, 255)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新雨滴位置
    for i in range(len(raindrops)):
        raindrops[i][1] += raindrops[i][2]
        if raindrops[i][1] > screen_height:
            raindrops[i][1] = 0
            raindrops[i][0] = random.randint(0, screen_width)

    # 清空屏幕
    screen.fill((0, 0, 0))

    # 绘制雨滴
    for raindrop in raindrops:
        pygame.draw.circle(screen, raindrop_color, (raindrop[0], raindrop[1]), 10)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()
