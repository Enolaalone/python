import pygame
import sys


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



            self.screen.fill((255,255,255))


            pygame.display.flip()  # 界面更新
            self.clock.tick(60)  # 60帧
        # -----退出
        pygame.quit()
        sys.exit()


Board().run()
