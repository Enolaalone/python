import pygame
import sys
import random



class Drop:  # 雨滴
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # 位置
        self.x = random.randint(0, self.screen_width)
        self.y = 0
        self.color = 'black'  # 颜色
        self.speed = random.randint(1, 10)  # 速度
        self.size = 10  # 大小

    def fall(self):
        self.y += self.size
        if self.y > self.screen_height:  # 越界处理
            self.y = 0
            self.x = random.randint(0, self.screen_width)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)  # 依附对象，颜色，圆心位置，大小


class Board:  # 界面
    def __init__(self, screen_width=1000, screen_height=800):  # 设置屏幕尺寸 长1000 宽800
        pygame.init()  # 初始化
        pygame.display.set_caption("Mirror")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True  # 游戏开始状态
        self.clock = pygame.time.Clock()  # 帧数

    def run(self):  # 运行
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # 界面颜色设计
            for x in range(self.screen_width):
                for y in range(self.screen_height):
                    # 根据像素的 x 坐标决定颜色
                    if x < self.screen_width // 2:
                        color = (255, 255, 255)  # 左半部分白色
                    else:
                        color = (0, 0, 0)  # 右半部分黑色
                    self.screen.set_at((x, y), color)  # 设置像素的颜色

            pygame.display.flip()  # 界面更新
            self.clock.tick(60)  # 60帧
        # -----退出
        pygame.quit()
        sys.exit()


Board().run()
