import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (125, 125, 135), (0, 0, 400, 400))
circle(screen, (207, 222, 44), (200, 200), 100)
circle(screen, (255, 0, 0), (165, 170), 30)
circle(screen, (255, 0, 0), (235, 170), 20)
circle(screen, (1, 1, 1), (165, 170), 10)
circle(screen, (1, 1, 1), (235, 170), 10)
rect(screen, (0, 0, 0), (150, 240, 100, 15))
polygon(screen, (0, 0, 0), [(180, 150), (190, 140), (120, 100), (110, 110)])
polygon(screen, (0, 0, 0), [(400-180, 150), (400-190, 140), (400-120, 100), (400-110, 110)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()