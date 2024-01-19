import pygame
import sys
import Data


class Column:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.Surface((Data.column[0], Data.column[1]))

    def pole(self):
        self.screen.blit(self.image, (self.x, self.y))
        pygame.draw.line(self.screen, (0, 0, 0), (self.x + Data.column[0] / 2, self.y),
                         (self.x + Data.column[0] / 2, self.y - Data.column[2]), 20)


class Square:
    def __init__(self, screen, x, y, size):

        self.screen = screen
        self.size = size
        self.x = x
        self.y = y
        self.image = pygame.Surface((3 * self.size, Data.square[2]), pygame.SRCALPHA)
        self.image.fill((225, 255, 255, 200))
        pygame.draw.rect(self.image, (100, 50, 200), (0, 0, 3 * self.size, Data.square[2]), 0)
        pygame.draw.rect(self.image, (255, 200, 255), (0, 0, 3 * self.size, Data.square[2]), 2)

        self.speed = Data.speed[0]

        self.move = False

    def update0(self, n, layer):
        if self.x != Data.tower[n] and self.y > (Data.columns[3] - Data.column[2] - Data.square[2]):
            self.y -= Data.speed[0]
            self.move = True
            # print(1)
            # print(Data.tower[n])
            # print(self.x)
        if self.x < Data.tower[n] and self.x != Data.tower[n] and self.y <= (
                Data.columns[3] - Data.column[2] - Data.square[2]):
            self.x += Data.speed[0]
            self.move = True
            # print(2)
            # print(self.x)
        if self.x > Data.tower[n] and self.x != Data.tower[n] and self.y <= (
                Data.columns[3] - Data.column[2] - Data.square[2]):
            self.x -= Data.speed[0]
            self.move = True
            # print(3)
            # print(self.x)
        if self.x == Data.tower[n] and self.y < (Data.columns[3] - Data.square[2] - Data.square[2] * layer):
            self.y += Data.speed[0]
            self.move = True
            # print(4)
            # print(Data.tower[n])
            # print(Data.columns[3]-Data.square[2]*layer)
            # print(self.y)
        if self.x == Data.tower[n] and self.y >= (Data.columns[3] - Data.square[2] - Data.square[2] * layer):
            self.move = False
            # print(5)

        self.screen.blit(self.image, (self.x - (3 / 2) * self.size, self.y))

    def show(self):
        self.screen.blit(self.image, (self.x - (3 / 2) * self.size, self.y))


class Table:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('汉诺塔')
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.clock = pygame.time.Clock()

        self.group_pole = []
        self.columns()

        self.group_square = []
        self.group_square_move = [[], [], []]
        self.square()
        self.hanoi_tower(Data.layer[0], 0, 1, 2)
        print(Data.move_x)

    def run(self):
        Data.move_x[0][0].move = True
        Data.move_x[0][3] = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            for i in self.group_pole:
                i.pole()

            for i in range(len(Data.move_x)):
                # print('i是',i)
                if Data.move_x[i][0].move:
                    if Data.move_x[i][3]:
                        # print(Data.move_x[i][0].size, Data.move_x[i][0].move)
                        # print(Data.move_x[i][1],Data.move_x[i][2])
                        Data.move_x[i][0].update0(Data.move_x[i][1], Data.move_x[i][2])
                        # print(Data.move_x[i][0].size, Data.move_x[i][0].move)
                        # print()
                        if not Data.move_x[i][0].move and ((i + 1) < len(Data.move_x)):
                            # print('yes')
                            Data.move_x[i + 1][0].move = True
                            Data.move_x[i][3] = False
                            if (i + 1) <= len(Data.move_x) - 1:
                                Data.move_x[i + 1][3] = True
                else:
                    Data.move_x[i][0].show()

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()

    def columns(self):
        for i in range(3):
            k = Column(self.screen, Data.columns[i], Data.columns[3])
            self.group_pole.append(k)

    def square(self):
        n = 0
        for i in range(Data.layer[0], 0, -1):
            n += 1
            k = Square(self.screen, Data.square[0], Data.square[1] - Data.square[2] * n, 15 * (i + 1))
            self.group_square.append(k)
        self.group_square_move[0] = self.group_square
        print(self.group_square_move)

    def move_position(self, a, c):
        A = []
        k = self.group_square_move[a].pop()
        A.append(k)
        A.append(c)
        A.append(len(self.group_square_move[c]))
        A.append(False)
        self.group_square_move[c].append(k)
        Data.move_x.append(A)
        print(A)

    def hanoi_tower(self, n, a, b, c):
        if n == 1:
            self.move_position(a, c)
        else:
            self.hanoi_tower(n - 1, a, c, b)
            self.move_position(a, c)
            self.hanoi_tower(n - 1, b, a, c)


if __name__ == '__main__':
    hanoi = Table(1000, 800)
    hanoi.run()
