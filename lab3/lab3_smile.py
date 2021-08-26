import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
FPS = 30
color = {'yellow': (242, 245, 66), 'red': (255, 0, 0), 'black': (0, 0, 0)}
x = y = 0


def drow_circle(color, x, y, r):
    """
    рисуем круг в центре экрана
    :param color: задает цвет фона круга
    :param x: координата х
    :param y: координата у
    :param r: радиус круга
    :return: None
    """
    circle(screen, color, (x, y), r)


def drow_line(color, x, y):
    """
    рисуем линии (брови и рот смайлика)
    :param color: цвет линии
    :param x: координата х
    :param y: координата у
    :return:  None
    """
    pass


drow_circle(color['yellow'], 200, 200, 130)
drow_circle(color['red'], 140, 170, 30)
drow_circle(color['black'], 140, 170, 13)
drow_circle(color['red'], 260, 170, 20)
drow_circle(color['black'], 260, 170, 10)
# drow_line()
# drow_line()
# drow_line()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
