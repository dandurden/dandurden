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


class NewBall:

    def __init__(self):
        self.x = randint(400, 800)
        self.y = randint(400, 800)
        self.r = randint(50, 100)
        self.color = COLORS[randint(0, 5)]
        self.xmax = self.x + self.r
        self.xmin = self.x - self.r
        self.ymax = self.y + self.r
        self.ymin = self.y - self.r

    def new_ball(self):
        '''рисует новый шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    ball = NewBall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ball.xmin < event.pos[0] < ball.xmax and \
                    ball.ymin < event.pos[1] < ball.ymax:
                print('click')
                pygame.display.update()
    ball.new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
