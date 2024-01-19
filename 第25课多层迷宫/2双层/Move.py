import pygame
import Data


class Subject(pygame.sprite.Sprite):  # 主体继承精灵类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # 继承精灵
        self.mao = pygame.image.load('mao.png').convert_alpha()  # 修改透明
        self.rect = self.mao.get_rect()  # 加载图像
        self.speed = 8  # 一次移动位移
        # ------------初始位置------------
        self.rect.x = Data.sb_rect[0]
        # print(Data.sb_rect[0])
        self.rect.y = Data.sb_rect[1]
        # print(Data.sb_rect[1])
        # -----------旧位置---------------------
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        # ------------游戏状态——---
        self.status = True

    def display(self, screen):
        screen.blit(self.mao, self.rect)

    def update(self, *args, **kwargs):
        if self.rect.y >= Data.game_over_y and self.rect.x >= Data.game_over_x:
            # print('游戏结束')
            self.status = False
        if self.status:
            key_press = pygame.key.get_pressed()
            # print(self.rect.x, self.rect.y)
            if key_press[pygame.K_w]:  # 享受
                # print(123)
                if self.rect.top > 0:
                    self.rect.y -= self.speed
            if key_press[pygame.K_s]:  # 向下
                if self.rect.bottom < pygame.display.get_surface().get_height():
                    self.rect.y += self.speed
            if key_press[pygame.K_a]:  # 享受
                if self.rect.left > 0:
                    self.rect.x -= self.speed
            if key_press[pygame.K_d]:  # 向下
                if self.rect.right < pygame.display.get_surface().get_width():
                    self.rect.x += self.speed

    def repeat(self):#返回初始位置
        # ------------初始位置------------
        self.rect.x = Data.sb_rect[0]
        # print(Data.sb_rect[0])
        self.rect.y = Data.sb_rect[1]
        # print(Data.sb_rect[1])
