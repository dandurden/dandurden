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

    def __init__(self, name='player'):
        self.score = 0
        self.name = input('имя нового игрока: ')

    def __add__(self, other):
        self.score += other


class NewBall:
    """
    этот класс предназначен для создания шарика с координатами x, y  и радуусом r,
    а также выбирает рандомный цвет из списка
    """

    def __init__(self):

        self.speedx = randint(5, 10)
        self.speedy = randint(5, 10)
        self.x = randint(103, 1097)
        self.y = randint(103, 797)
        self.r = randint(50, 100)
        self.color = COLORS[randint(0, 5)]

    def new_ball(self):
        '''рисует новый шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)

    def new_fig(self):
        rect(screen, self.color, (self.x, self.y, self.r, self.r))

    def move_ball(self):
        """двигает шарик и отражает от стен"""
        self.x += self.speedx
        self.y += self.speedy
        if self.y + self.r >= 900 or self.y - self.r <= 0:
            self.speedy *= -1
        if self.x + self.r >= 1200 or self.x - self.r <= 0:
            self.speedx *= -1

    def move_fig(self):
        """двигает квадрат и отражает от стен"""
        self.x += self.speedx
        self.y += self.speedy
        if self.y + self.r >= 900 or self.y <= 0:
            self.speedy *= -1
        if self.x + self.r >= 1200 or self.x <= 0:
            self.speedx *= -1

# balls создать список шариков
balls = [NewBall(), NewBall(), NewBall(), NewBall(), NewBall()]
fig = NewBall()
game = Newgame()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for ball in balls[:3]:
        ball.new_ball()
    for fig in balls[3:]:
        fig.new_fig()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            for ball in balls:

                if ball.x - ball.r < pos[0] < ball.x + ball.r and \
                        ball.y - ball.r < pos[1] < ball.y + ball.r:  # и клик попал в диапазон (площадь) шарика
                    if ball in balls[:3]:
                        game + 1
                        print(f"{game.name} = {game.score}")
                        pygame.display.update()

                    else:
                        game + 5
                        print(f"{game.name} = {game.score}")
                        pygame.display.update()

    for ball in balls[:3]:
        ball.move_ball()
    for fig in balls[3:]:
        fig.move_fig()
    pygame.display.update()

    screen.fill(BLACK)

pygame.quit()
