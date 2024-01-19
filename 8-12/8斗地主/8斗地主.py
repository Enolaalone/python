import Date
import sys
import pygame
import random


class Table:
    def __init__(self, width=960, height=540):
        pygame.init()
        pygame.display.set_caption('斗地主')
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.clock = pygame.time.Clock()

        self.C = []
        self.cards_1()
        self.cards_sequence()


        self.bg = pygame.image.load('game.png')

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.bg, (0, 0))
            self.draw_card_1()

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()

    def cards_1(self):
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

    def draw_card_1(self):
        for i in range(len(self.C)):
            k = Card(self.screen, 150 + 30 * i, 400, 90, self.C[i])
            k.draw_card()


class Card:
    def __init__(self, screen, x, y, size, text, word=25):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.text = text

        self.word = word
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, word)

        self.up = False

    def draw_card(self):
        self.card = pygame.Surface((self.size, (3 / 2) * self.size), pygame.SRCALPHA)

        self.card.fill((255, 255, 255, 0))
        pygame.draw.rect(self.card, (255, 255, 255), (0, 0, self.size, (3 / 2) * self.size), width=0, border_radius=10)
        pygame.draw.rect(self.card, (0, 0, 0), (0, 0, self.size, (3 / 2) * self.size), width=1, border_radius=10)
        self.read()
        self.screen.blit(self.card, (self.x, self.y))

    def read(self):
        B = ['\u2665', '\u2666', '\u2663', '\u2660']
        A = self.text.split('\n')

        n = 0
        for i in A:
            self.font = pygame.font.Font(self.font_name, self.word)

            if '\u2665' in A or '\u2666' in A:
                colors = 'red'
            else:
                colors = 'black'

            txt = self.font.render(i, True, colors)
            self.card.blit(txt, (5, 10 + 20 * n))
            n += 1

            if i in B:
                self.font = pygame.font.Font(self.font_name, 100)
                txt2 = self.font.render(i, True, colors)
                self.card.blit(txt2, (self.size / 4, 0))

if __name__ == '__main__':
    game=Table()
    game.run()