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

screen.fill((174, 244, 245))  # закрасили фон

rect(screen, color['green'], ((0, y/2), (x, y/2)))




pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
