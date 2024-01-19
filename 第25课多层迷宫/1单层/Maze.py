import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))#填充黑色
        self.rect=self.image.get_rect()#返回位置
        self.rect.x=x
        self.rect.y=y



