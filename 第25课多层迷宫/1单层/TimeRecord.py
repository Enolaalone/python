import pygame


class TimeR:
    def __init__(self, screen):
        self.screen = screen  # 屏幕
        self.paused = False  # 时间是否停止
        self.begin_time = 0  # 初始时间
        self.end_time = 0  # 结束时间
        self.font = pygame.font.Font(None, 50)  # 时间字体

    def b_record(self):
        self.begin_time = (pygame.time.get_ticks() / 1000)  # 记录下最新起始时间，转化成秒

    def record(self):
        if not self.paused:  # 如果时间不停
            tm_1 = pygame.time.get_ticks()  # 获取当下时间
            second = int(tm_1 / 1000) - self.begin_time  # 时间差
            time_txt1 = self.font.render(f'Time:{second}s', True, (0, 0, 0))  # 渲染时间成图像
            self.screen.blit(time_txt1, (0, 0))  # 将渲染的图像贴到左上原点
        else:#时间停止

            time_txt2=self.font.render(f'Congratulate! Take {(self.end_time-self.begin_time):.0f}s.',True,(0,0,0))
            self.screen.blit(time_txt2,(pygame.display.get_surface().get_width()/4,0))


