import pygame

pygame.init()

# 创建游戏窗口
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 创建一个图像表面
surface = pygame.Surface((200, 100))

# 绘制红色矩形在图像表面上
red = (255, 0, 0)
pygame.draw.rect(surface, red, (0, 0, 200, 100))

# 定义矩形在游戏窗口上的位置
rect_x, rect_y = 300, 250

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清空屏幕
    screen.fill((0, 0, 0))

    # 将图像表面绘制到游戏窗口上
    screen.blit(surface, (rect_x, rect_y))

    # 更新游戏窗口显示
    pygame.display.flip()

pygame.quit()
