import pygame
import sys


class Txt:
    def __init__(self,x,y,width,height,text,screen,color='black'):
        self.screen=screen
        self.font=pygame.font.Font(None,350)
        self.input_box=pygame.Rect(x,y,width,height)
        self.color=color
        self.text=text
        self.status = True

    def write(self):
        if self.status:
            txt_surface = self.font.render(self.text, True, self.color)
            self.screen.blit(txt_surface, (self.input_box.x, self.input_box.y))



class Board:  # 界面
    def __init__(self, screen_width=1000, screen_height=800):  # 设置屏幕尺寸 长1000 宽800
        pygame.init()  # 初始化
        pygame.display.set_caption("Mirror")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True  # 游戏开始状态
        self.clock = pygame.time.Clock()  # 帧数
        #--------------------------------------
        # self.font=pygame.font.Font(None,350)
        # self.input_box=pygame.Rect(self.screen_width//8,self.screen_height//4,self.screen_width//2,100)
        self.text1=Txt(self.screen_width//8,self.screen_height//4,self.screen_width//4,self.screen_height//4,'Mir',self.screen)
        self.text2=Txt(4*(self.screen_width//8),self.screen_height//4,self.screen_width//4,self.screen_height//4,'ror',self.screen)

        # self.inactive=pygame.Color('red')
        # self.active=pygame.Color('black')
        # self.color=self.inactive
        # self.status=False
        # self.text='Mir'


    def run(self):  # 运行
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.text1.status=False
                        self.text2.status=False

            self.screen.fill((255, 255, 255))

            # txt_surface=self.font.render(self.text,True,self.color)
            # self.screen.blit(txt_surface,(self.input_box.x,self.input_box.y))
            self.text1.write()
            self.text2.write()

            pygame.display.flip()  # 界面更新
            self.clock.tick(60)  # 60帧
        # -----退出
        pygame.quit()
        sys.exit()


Board().run()
