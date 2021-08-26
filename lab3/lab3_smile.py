import pygame
from pygame.draw import *

pygame.init()
FPS = 30


def drow_circle(color, x, y):
    """
    рисуем круг в центре экрана
    :param color: задает цвет фона круга
    :param x: координата х
    :param y: координата у
    :return: None
    """
    pass


def drow_line(color, x, y):
    """
    рисуем линии (брови и рот смайлика)
    :param color: цвет линии
    :param x: координата х
    :param y: координата у
    :return:  None
    """
    pass


drow_circle()
drow_circle()
drow_circle()
drow_circle()
drow_circle()
drow_line()
drow_line()
drow_line()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
