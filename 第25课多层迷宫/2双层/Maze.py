import pygame
import Data

class Wall(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))#填充黑色
        self.rect=self.image.get_rect()#返回位置
        self.rect.x=x
        self.rect.y=y


class Walls:
    def __init__(self,screen,A):
        self.screen=screen
        self.walls = pygame.sprite.Group()  # 将墙作为类
        self.number = A #迷宫组
        #-------添加精灵组-----------
        self.wall_s(self.number)
        # print(self.number)

    def wall_s(self, A):  # 添加墙精灵组
        for i in range(len(A)):
            k = Wall(self.screen, A[i][0], A[i][1], A[i][2], A[i][3])
            self.walls.add(k)  # 添加到组

    def drawing(self):
        self.walls.draw(self.screen)


