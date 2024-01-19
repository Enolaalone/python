import pygame
import sys


class Text:
    def __init__(self,screen, x, y, text):
        self.screen = screen
        self.x=x
        self.y=y
        self.font_name = pygame.font.match_font('simsun')
        self.font = pygame.font.Font(self.font_name, 100)
        self.text = self.font.render(text, True, (255, 0, 0))

    def show(self):
        self.screen.blit(self.text, (self.x, self.y))


class TimeRecord:
    def __init__(self):
        self.begin_time =0
        self.end_time =0
        self.second=0
        self.paused=False

    def b_record(self):
        self.begin_time = pygame.time.get_ticks()/1000

    def e_record(self):
        self.end_time = pygame.time.get_ticks()/1000

    def record(self):
        print('123')
        tm=int(pygame.time.get_ticks()/1000)
        self.second=tm-self.begin_time

    def show(self,screen,x,y):
        if not self.paused:
            Text(screen,x,y,f'{self.second:.0f}').show()
        else:
            Text(screen,x,y,f'{self.end_time-self.begin_time:.0f}').show()


class Table:
    def __init__(self, width=1000, height=800):
        pygame.init()
        pygame.display.set_caption('抢十')
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.running = True
        self.game_status=False
        self.clock = pygame.time.Clock()

        self.txt_0=Text(self.screen, width/4, height/4,'抢10大比拼')
        self.txt_1=Text(self.screen, width/5, height/2,'点击开始游戏')
        self.txt_2=Text(self.screen, width/4, height/2,'游戏失败')
        self.time=TimeRecord()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    if not self.game_status:
                        self.game_status=True
                        self.time.paused=False
                        self.time.b_record()
                    else:
                        self.game_status=False
                        self.time.paused=True
                        self.time.e_record()
                    
            self.screen.fill((255,255, 255))

            self.txt_0.show()
            if not self.game_status and not self.time.paused:
                self.txt_1.show()

            if not self.time.paused and self.game_status:
                self.time.record()
                if self.time.second<=10:
                    self.time.show(self.screen,self.width*(1/2),self.height/2)
                else:
                    self.txt_2.show()

            if self.time.paused and not self.game_status:
                self.time.show(self.screen,self.width*(1/2),self.height/2)

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    table = Table()
    table.run()