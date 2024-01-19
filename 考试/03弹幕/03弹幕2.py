import pygame
import sys
import random


class Text:
    def __init__(self, screen):
        self.screen = screen
        self.A = []
        self.read()
        self.random()

    def read(self):
        f = open('弹幕.txt', 'r', encoding='utf-8')
        a = f.readlines()
        for i in a:
            self.A.append(i)
        f.close()

    def random(self):
        self.x = 0
        self.y = random.randint(20, 400)
        self.text = self.A[random.randint(0, len(self.A) - 1)]
        self.color = (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
        self.speed = random.randint(4, 10)
        self.font = pygame.font.Font(None, random.randint(40, 80))

    def web(self):
        txt = self.font.render(self.text, True,self.color)
        self.screen.blit(txt, (self.x, self.y))
        self.x += self.speed
        if self.x > self.screen.get_width():
            self.random()

    def color_random(self):
        self.color = (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))


class Table:
    def __init__(self, width=1000, height=800):
        pygame.init()
        pygame.display.set_caption('弹幕')
        self.running = True

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.txts = []
        self.txts2 = []
        self.txt_setting()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))

            for i in self.txts:
                i.web()
            for i in self.txts2:
                i.web()
                i.color_random()

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()

    def txt_setting(self):
        for i in range(15):
            self.txts.append(Text(self.screen))
        for i in range(5):
            self.txts2.append(Text(self.screen))


if __name__ == '__main__':
    table = Table()
    table.run()
