import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Newgame:

    def __init__(self):
        self.score = 0

    def __add__(self, other):
        self.score += other


class NewBall:
    """
    этот класс предназначен для создания шарика с координатами x, y  и радуусом r,
    а также выбирает рандомный цвет из списка
    """

    def __init__(self):
        self.speedx = 5
        self.speedy = 3
        self.x = randint(903, 1097)
        self.y = randint(603, 797)
        self.r = randint(50, 100)
        self.color = COLORS[randint(0, 5)]
        self.xmax = self.x + self.r
        self.xmin = self.x - self.r
        self.ymax = self.y + self.r
        self.ymin = self.y - self.r

    def new_ball(self):
        '''рисует новый шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)

    def move_ball(self):
        """двигает шарик и отражает от стен"""
        self.x += self.speedx
        self.y += self.speedy
        if self.y + self.r >= 900 or self.y - self.r <= 0:
            self.speedy *= -1
        if self.x + self.r >= 1200 or self.x - self.r <= 0:
            self.speedx *= -1

ball_1 = NewBall()

game = Newgame()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    ball_1.new_ball()  # создаем новый шарик

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print((ball_1.xmax, ball_1.ymax, ball_1.xmin, ball_1.ymin))# если кликнули мышкой
            if ball_1.xmin < event.pos[0] < ball_1.xmax and \
                    ball_1.ymin < event.pos[1] < ball_1.ymax:  # и клик попал в диапазон (площадь) шарика
                game + 1
                print(game.score)
                pygame.display.update()
    ball_1.move_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
