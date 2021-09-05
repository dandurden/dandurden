import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
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
        self.x = randint(600, 1100)
        self.y = randint(400, 800)
        self.r = randint(50, 100)
        self.color = COLORS[randint(0, 5)]
        self.xmax = self.x + self.r
        self.xmin = self.x - self.r
        self.ymax = self.y + self.r
        self.ymin = self.y - self.r
        self.counter = 0

    def new_ball(self):
        '''рисует новый шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)


game = Newgame()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    ball = NewBall()  # создали экземпляр класса
    ball.new_ball()  # создаем новый шарик
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если кликнули мышкой
            if ball.xmin < event.pos[0] < ball.xmax and \
                    ball.ymin < event.pos[1] < ball.ymax:  # и клик попал в диапазон (площадь) шарика
                game + 1
                print(game.score)
                pygame.display.update()

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
