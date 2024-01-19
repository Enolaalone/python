import pygame
import sys

class TimeCheck:
    def __init__(self,screen):
        self.screen=screen
        self.paused=False
        self.begin_time=0#初始时间
    def time_get(self,font):
        if not self.paused:
            # 获取游戏持续时间
            ticks = pygame.time.get_ticks()
            seconds = int(ticks / 1000)-self.begin_time # 将毫秒转换成秒
            # print(123)
            # 将时间渲染为图像
            timer_text = font.render(f"Time: {seconds} S", True, (0, 0, 0))
            # 绘制时间
            self.screen.blit(timer_text, (0, 0))  # 将文本绘制到屏幕上
        else:
            end_time=pygame.time.get_ticks()/1000-self.begin_time
            # 将时间渲染为图像
            timer_text = font.render(f"Time: {end_time} S", True, (0, 0, 0))
            # 绘制时间
            self.screen.blit(timer_text, (0, 0))  # 将文本绘制到屏幕上



class Board:  # 界面
    def __init__(self, screen_width=1000, screen_height=800):  # 设置屏幕尺寸 长1000 宽800
        pygame.init()  # 初始化
        pygame.display.set_caption("Mirror")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True  # 游戏开始状态
        self.clock = pygame.time.Clock()  # 帧数
        #-------------
        self.tm=TimeCheck(self.screen)
        self.font = pygame.font.Font(None, 36)

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

            self.tm.time_get(self.font)

            pygame.display.flip()  # 界面更新
            self.clock.tick(60)  # 60帧
        # -----退出
        pygame.quit()
        sys.exit()


Board().run()
