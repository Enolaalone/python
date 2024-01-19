import sys
import pygame
import Maze  # 导入迷宫墙
import Move  # 导入移动对象
import TimeRecord  # 导入时间模块
import Data  # 导入数据


class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('迷宫')
        self.screen = pygame.display.set_mode((Data.screen_width, Data.screen_height))
        self.clock = pygame.time.Clock()  # 加入帧数
        self.running = True
        self.tm = TimeRecord.TimeR(self.screen)  # 计时模块
        self.sb = Move.Subject()  # 人物模块
        self.wall1 = Maze.Walls(self.screen, Data.A)  # 墙精灵类-----------
        # ---------------一层-------------------
        self.lines = 1  # 层数

    def run(self):
        while self.running:
            for event in pygame.event.get():  # 获取屏幕的事件
                if event.type == pygame.QUIT:  # 退出
                    self.running = False
                if not self.sb.status and not self.tm.paused:
                    if self.lines == 1:
                        self.lines = 2
                        self.sb.repeat()#返回初始位置
                        self.sb.status=True#重启人物

                    if self.lines == 2 and not self.sb.status:
                        # print('y')
                        self.tm.end_time = pygame.time.get_ticks() / 1000
                        self.tm.paused = True  # 时间停止

            self.sb.update()  # 检测人物活动

            self.screen.fill((255, 255, 255))
            self.tm.record()  # 计时
            self.sb.display(self.screen)  # 展示人物

            if self.lines == 1:  # 一层
                self.wall1.drawing()  # 显示墙
                self.collide(self.wall1.walls)
            if self.lines == 2:  # 两层
                self.wall1 = Maze.Walls(self.screen, Data.B)  # 墙精灵类-----------
                self.wall1.drawing()  # 显示墙
                self.collide(self.wall1.walls)
            pygame.display.flip()  # 显示

            # --------------获取就位置
            self.sb.old_x = self.sb.rect.x
            self.sb.old_y = self.sb.rect.y

            self.clock.tick(30)  # 30帧
        pygame.quit()  # 结束
        sys.exit()  # 退出

    def collide(self, wall):  # 碰撞检测
        # 检测碰撞
        collisions = pygame.sprite.spritecollide(self.sb, wall, False)
        if collisions:  # 返回旧位置
            self.sb.rect.x = self.sb.old_x
            self.sb.rect.y = self.sb.old_y


Board().run()
