import pygame
import sys
import TimeRecord#导入时间模块


class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('迷宫')
        screen_width = 800
        screen_height = 600
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()  # 加入帧数
        self.running = True
        self.tm=TimeRecord.TimeR(self.screen)



    def run(self):
        while self.running:
            for event in pygame.event.get():  # 获取屏幕的事件
                if event.type == pygame.QUIT:  # 退出
                    self.running = False
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if event.button ==1:
                        self.tm.end_time=pygame.time.get_ticks()/1000
                        self.tm.paused=True#时间停止
            self.screen.fill((255,255,255))
            self.tm.record()

            pygame.display.flip()  # 显示
            self.clock.tick(30)  # 30帧
        pygame.quit()  # 结束
        sys.exit()  # 退出


Board().run()
