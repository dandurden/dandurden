import pygame
from pygame.draw import *

pygame.init()
x = 800  # ширина
y = 600  # высота
screen = pygame.display.set_mode((x, y))
FPS = 30
color = {'yellow': (242, 245, 66),
         'pink': (224, 61, 36),
         'green': (105, 196, 96),
         'dark_green': (57, 102, 53),
         'white': (255, 255, 255),
         'brown': (158, 119, 85),
         'ligth_brown': (163, 138, 70),
         'blue': (125, 174, 212)}

# закрасили фон
screen.fill((174, 244, 245))
# нарисовали траву
rect(screen, color['green'], ((0, y / 2), (x, y / 2)))


def draw_cloud(x, y, r):
    """
    эта функция рисует облака по заданным координатам и радиусу
    :param x: координата х
    :param y: координата у
    :param r: радиус облачка
    :return:
    """
    for i in [0 * r, r, 2 * r, 3 * r]:
        if i == r or i == 2 * r:
            circle(screen, color['white'], (x + i, y), r)
            circle(screen, color['white'], (x + i, y - r), r)
        else:
            circle(screen, color['white'], (x + i, y), r)


def draw_house(x, y, wedth, height):
    """
    функция рисует домик с окном и треугольной крышей в средине
    :param x: начальная координата x (где рисовать)
    :param y: начальная координата y (где рисовать)
    :param wedth: ширина домика
    :param height: высота домика
    :return:
    """
    rect(screen, color['brown'], (x, y, wedth, height))  # корпус (стеныб каркас)
    polygon(screen, color['pink'], [(x, y), (x+wedth/2, wedth), (x+wedth, y)])  # крыша
    rect(screen, color['blue'], (x + wedth/4, y + height/3, wedth/2, height/3))  # (окно)


def draw_frees(x, y, r):
    """
    эта функция рисует деревья
    :param x: координата х
    :param y: координата у
    :param r: радиус круга дерева (листва)
    :return:
    """
    for i in [0 * r, r, 2 * r, 2.5 * r]:
        if i == r or i == 2.5 * r:
            circle(screen, color['dark_green'], (x - r, y + i), r)
            circle(screen, color['dark_green'], (x + r, y + i), r)
        else:
            circle(screen, color['dark_green'], (x, y + i), r)
    line(screen, color['ligth_brown'], (x, y + 3*r), (x, y + 6*r), r)


draw_cloud(100, 90, 20)
draw_cloud(400, 135, 15)
draw_cloud(650, 100, 20)
# нарисовал солнце
circle(screen, color['yellow'], (35, 35), 25)
# рисуем дом 1
draw_house(70, 350, 200, 180)
# рисуем дом 2
draw_house(500, 250, 140, 120)
# рисуем деревья
draw_frees(350, 250, 30)
draw_frees(720, 200, 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
