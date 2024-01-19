import sys
import pygame
import Data


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))
        pygame.draw.circle(self.image, color, (15, 15), 15, 0)
        self.rect = self.image.get_rect()
        screen.blit(self.image, (self.x - 15, self.y - 15))


class Balls(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.group = pygame.sprite.Group()

    def ball_add(self):
        for i in range(len(Data.balls)):
            ball = Ball(Data.balls[i][2], self.screen, Data.balls[i][0], Data.balls[i][1])
            self.group.add(ball)


class Table:
    def __init__(self, width=1000, height=600):
        pygame.init()
        pygame.display.set_caption('台球')
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.rect_width = 45

    def dot(self):
        for i in range(len(Data.dot)):
            pygame.draw.circle(self.screen, (255, 255, 255), Data.dot[i], 5, 0)

    def dig(self):
        for i in range(len(Data.dig)):
            pygame.draw.circle(self.screen, (0, 0, 0), Data.dig[i], 25, 0)

    def rect(self):
        pygame.draw.rect(self.screen, (34, 139, 34), (0, 0, self.width, self.height), 0, border_radius=20)
        pygame.draw.rect(self.screen, (139, 71, 38), (0, 0, self.width, self.height), self.rect_width, border_radius=20)

    def lines(self):
        pygame.draw.line(self.screen, (0, 0, 0), (0.25 * self.width, self.rect_width), (0.25 * self.width, self
                                                                                        .height - self.rect_width), 3)
        pygame.draw.circle(self.screen, (0, 0, 0), [0.25 * self.width, 0.5 * self.height], 100, 3, draw_top_left=True,
                           draw_bottom_left=True)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.rect()
            self.dig()
            self.dot()
            self.lines()

            Balls(self.screen).ball_add()

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    table = Table()
    table.run()
