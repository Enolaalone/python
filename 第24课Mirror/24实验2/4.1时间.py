import pygame
import sys

# 初始化 Pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))

# 设置字体
font = pygame.font.Font(None, 36)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取游戏持续时间
    ticks = pygame.time.get_ticks()
    seconds = int(ticks / 1000)  # 将毫秒转换成秒

    # 将时间渲染为图像
    timer_text = font.render(f"Time: {seconds} seconds", True, (255, 255, 255))

    # 绘制时间
    screen.fill((0, 0, 0))  # 用黑色填充屏幕
    screen.blit(timer_text, (10, 10))  # 将文本绘制到屏幕上

    pygame.display.flip()  # 更新屏幕显示

# 退出 Pygame
pygame.quit()
sys.exit()
