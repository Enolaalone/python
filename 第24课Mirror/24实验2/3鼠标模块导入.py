import pygame
import sys


class MouseCursor:
    def __init__(self, screen):
        self.screen = screen#当前屏幕
        self.mouse_x, self.mouse_y = 0, 0#初始鼠标值

    def handle_events(self,event):
        # for event in pygame.event.get():#检测鼠标移动事件
            if event.type == pygame.MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos

    def draw(self):
        # self.screen.fill((0, 0, 0))
        r = 10
        if self.mouse_x < self.screen.get_width() // 2:
            pygame.draw.circle(self.screen, (173, 216, 230), (self.mouse_x, self.mouse_y), r)
            pygame.draw.circle(self.screen, (255, 192, 203), (self.screen.get_width() - self.mouse_x, self.mouse_y), r)
        else:
            pygame.draw.circle(self.screen, (255, 192, 203), (self.mouse_x, self.mouse_y), r)
            pygame.draw.circle(self.screen, (173, 216, 230), (self.screen.get_width() - self.mouse_x, self.mouse_y), r)


class Board:  # 界面
    def __init__(self, screen_width=1000, screen_height=800):  # 设置屏幕尺寸 长1000 宽800
        pygame.init()  # 初始化
        pygame.display.set_caption("Mirror")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True  # 游戏开始状态
        self.clock = pygame.time.Clock()  # 帧数

        self.cursor = MouseCursor(self.screen)#鼠标对象

    def run(self):  # 运行
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.cursor.handle_events(event)#检测

            self.cursor.draw()#鼠标绘制


            # # 界面颜色设计
            # for x in range(self.screen_width):
            #     for y in range(self.screen_height):
            #         # 根据像素的 x 坐标决定颜色
            #         if x < self.screen_width // 2:
            #             color = (255, 255, 255)  # 左半部分白色
            #         else:
            #             color = (0, 0, 0)  # 右半部分黑色
            #         self.screen.set_at((x, y), color)  # 设置像素的颜色


            pygame.display.flip()  # 界面更新
            self.clock.tick(60)  # 60帧
        # -----退出
        pygame.quit()
        sys.exit()


Board().run()
