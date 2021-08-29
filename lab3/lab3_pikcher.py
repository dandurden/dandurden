import pygame
from pygame.draw import *

pygame.init()
x = 800  # ширина
y = 600  # высота
screen = pygame.display.set_mode((x, y))
FPS = 30
color = {'yellow': (242, 245, 66),
         'pink': (240, 60, 141),
         'green': (105, 196, 96),
         'dark_green': (57, 102, 53),
         'white': (255, 255, 255),
         'brown': (71, 68, 29),
         'ligth_brown': (163, 138, 70)}

# закрасили фон
screen.fill((174, 244, 245))
# нарисовали траву
rect(screen, color['green'], ((0, y / 2), (x, y / 2)))


def draw_cloud(x, y, r):
    """

    :param x: координата х
    :param y: координата у
    :param r: радиус облачка
    :return:
    """
    if r > 15:
        for i in [0, 20, 40, 60]:
            if i == 20 or i == 40:
                circle(screen, color['white'], (x + i, y), r)
                circle(screen, color['white'], (x + i, y - r), r)
            else:
                circle(screen, color['white'], (x + i, y), r)
    else:
        for i in [0, 15, 30, 45]:
            if i == 15 or i == 30:
                circle(screen, color['white'], (x + i, y), r)
                circle(screen, color['white'], (x + i, y - r), r)
            else:
                circle(screen, color['white'], (x + i, y), r)


draw_cloud(100, 90, 20)
draw_cloud(400, 135, 15)
draw_cloud(650, 100, 20)
# нарисовал солнце
circle(screen, color['yellow'], (35, 35), 25)
# рисуем дом


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
