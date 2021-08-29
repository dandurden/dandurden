import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
FPS = 30
color = {'yellow': (242, 245, 66), 'red': (255, 0, 0), 'black': (0, 0, 0)}

screen.fill((120, 120, 120))  # закрасили фон серым цветом


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


def drow_line(color, x, y, x1, y1=0, width=1, incline=False):
    """
    рисуем линии (брови и рот смайлика)
    :param incline: наклон (да/нет)
    :param width: ширина линии
    :param x1: новая координата (конец линии)
    :param y1: новая координата (конец линии)
    :param color: цвет линии
    :param x: координата х (начало линии)
    :param y: координата у (начало линии)
    :return:  None
    """
    if not incline:
        line(screen, color, (x, y), (x1, y), width)
    else:
        line(screen, color, (x, y), (x1, y1), width)


drow_circle(color['yellow'], 200, 200, 130)
drow_circle(color['red'], 140, 170, 30)
drow_circle(color['black'], 140, 170, 13)
drow_circle(color['red'], 260, 170, 20)
drow_circle(color['black'], 260, 170, 10)
drow_line(color['black'], 140, 270, 260, 270, 25)
drow_line(color['black'], 80, 95, 180, 150, 17, incline=True)
drow_line(color['black'], 330, 112, 220, 155, 17, incline=True)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
