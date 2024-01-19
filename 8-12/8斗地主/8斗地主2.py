import sys
import pygame
import Date
import random


class Table():
    def __init__(self, width=960, height=540):
        pygame.init()
        pygame.display.set_caption('斗地主')
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.clock = pygame.time.Clock()

        self.host = Landlord(self.screen)

        self.bg = pygame.image.load('game.png')


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # print(mouse_pos)
                    for sprite in self.host.c_1:
                        if sprite.rect.collidepoint(mouse_pos) and event.button == 1:
                            print(123)
                            if not sprite.up:
                                print(1)
                                sprite.up = True
                                break
                            if sprite.up:
                                print(2)
                                sprite.up = False
                                break

            self.screen.blit(self.bg, (0, 0))

            self.host.draw_cards_1()

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()


class Card(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, size, text, word=25):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.text = text

        self.word = word
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, word)

        self.up = False
        self.last = False

        if not self.last:
            self.rect = pygame.Rect(self.x, self.y, 30, (3 / 2) * self.size)
        else:
            self.rect = pygame.Rect(self.x, self.y, self.size, (3 / 2) * self.size)

        # print(pygame.font.get_fonts())

    def draw_card(self):
        self.card = pygame.Surface((self.size, (3 / 2) * self.size), pygame.SRCALPHA)
        self.card.fill((255, 255, 255, 0))
        pygame.draw.rect(self.card, (255, 255, 255), (0, 0, self.size, (3 / 2) * self.size), 0, border_radius=10)
        pygame.draw.rect(self.card, (0, 0, 0), (0, 0, self.size, (3 / 2) * self.size), 1, border_radius=10)
        self.read()
        if not self.up:
            self.screen.blit(self.card, (self.x, self.y))
        if self.up:
            self.screen.blit(self.card, (self.x, self.y - 20))

    def read(self):
        B = ['\u2665', '\u2666', '\u2660', '\u2663']
        A = self.text.split('\n')
        # print(A)
        n = 0
        for i in A:
            self.font = pygame.font.Font(self.font_name, self.word)
            # print(i)

            if '\u2665' in A or '\u2666' in A:
                colors = 'red'
            else:
                colors = 'black'

            txt = self.font.render(i, True, colors)
            self.card.blit(txt, (5, 10 + 20 * n))
            n += 1

            if i in B:
                # print('yes')
                self.font = pygame.font.Font(self.font_name, 100)
                txt2 = self.font.render(i, True, colors)
                self.card.blit(txt2, (self.size / 4, 0))


class Landlord(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.C = []
        self.c_1 = pygame.sprite.Group()
        self.cards_set()
        self.cards_sequence()
        self.group_set()

    def cards_set(self):
        for i in range(20):
            k = random.randint(0, len(Date.pk1) - 1)
            self.C.append(Date.pk1[k])
            del Date.pk1[k]

    def cards_sequence(self):
        for i in range(len(self.C) - 1):
            f = i
            for j in range(i + 1, len(self.C)):
                if Date.pk3[self.C[j]] == Date.pk3[self.C[f]]:
                    if Date.pk4[self.C[j]] > Date.pk4[self.C[f]]:
                        f = j

                if Date.pk3[self.C[j]] > Date.pk3[self.C[f]]:
                    f = j
            if f != i:
                self.C[f], self.C[i] = self.C[i], self.C[f]

    def group_set(self):
        for i in range(len(self.C)):
            k = Card(self.screen, 100 + 30 * i, 400, 90, self.C[i])
            if i == len(self.C) - 1:
                print('yes')
                k.last = True
            self.c_1.add(k)

    def draw_cards_1(self):
        for k in self.c_1:
            k.draw_card()


if __name__ == "__main__":
    table = Table()
    table.run()
