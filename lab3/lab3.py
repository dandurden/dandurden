import pygame
from pygame.draw import *
# инициализация библиотеки
pygame.init()
# создаем окно
screen = pygame.display.set_mode((400, 400))
# добавляем небольшую задержку в галвный цикл программы
clock = pygame.time.Clock()
# устанавливаем FPS  в 30 кдаров секунду
FPS = 30

# рисуем фигурки
rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100, 100), (200, 50),
                                (300, 100), (100, 100)])
polygon(screen, (0, 0, 255), [(100, 100), (200, 50),
                                (300, 100), (100, 100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)


# после того чтоб отобразить на экране нужно обновить экран
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
finnished = False
while not finnished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finnished = True

pygame.quit()
