# first attempt

import pygame
from pygame.draw import *

pygame.init()

FPS = 30


def draw_picture(screen):
    '''
    Drawing the picture
    param screen: the surface to draw on
    return: None
    '''
    small_cats_positions = [(100, 500), (400, 600), (300, 450), (550, 520)]
    chukchi_positions = [(700, 320), (780, 250), (940, 330), (960, 500)]
    igloo_positions = [(80, 350), (530, 350), (600, 450)]

    for current_igloo in igloo_positions:
        igloo(screen, 80, current_igloo)

    for current_chukcha in chukchi_positions:
        chukchi(screen, 200, current_chukcha)

    # big igloo and big chukcha
    chukchi(screen, 400, (800, 300))
    igloo(screen, 200, (300, 400))

    for current_cat in small_cats_positions:
        cat(screen, 200, current_cat)


def inclined_hand(surf, size, pos):
    '''
    Drawing left inclined hand of chukcha
    param surf: surface to draw on
    param size: scale factor, apply the same hand size as body size
    param pos: list of x and y coordinates to place on the surface, apply the same hand position as chukchi position
    return: None
    '''
    color = (223, 223, 223)
    brown = (222, 188, 153)
    surface = pygame.Surface((int(0.05 * size), int(0.125 * size)))
    surface.fill(color)
    ellipse(surface, brown, (0, 0, int(0.05 * size), int(0.125 * size)), 0)
    surface2 = pygame.transform.rotate(surface, 45)
    surf.blit(surface2, (int(pos[0] + 0.18 * size), int(pos[1] + 0.37 * size)))


def chukchi_body(surf, size, pos):
    '''
    Drawing body of the chukchi
    param surf: surface to draw on
    param size: scale factor, apply the same body size as chukchi size
    param pos: list of x and y coordinates to place on the surface, apply the same body position as chukchi position
    return: None
    '''
    color = (223, 223, 223)
    brown = (222, 188, 153)
    dark_brown = (167, 133, 106)
    light = (220, 208, 186)

    circle(surf, light, (int(pos[0] + 0.15 * size), int(pos[1] + 0.25 * size)), int(0.1 * size), 0)
    ellipse(surf, brown, (int(pos[0] + 0.05 * size), int(pos[1] + 0.25 * size), int(0.2 * size), int(0.75 * size)))
    ellipse(surf, brown, (int(pos[0]), int(pos[1] + 0.4 * size), int(0.125 * size), int(0.05 * size)), 0)
    rect(surf, color, (int(pos[0] + 0.05 * size), int(pos[1] + 0.625 * size), int(0.2 * size), int(0.375 * size)), 0)
    ellipse(surf, brown, (int(pos[0] + 0.08 * size), int(pos[1] + 0.58 * size), int(0.05 * size), int(0.12 * size)), 0)
    ellipse(surf, brown, (int(pos[0] + 0.17 * size), int(pos[1] + 0.58 * size), int(0.05 * size), int(0.12 * size)), 0)
    ellipse(surf, brown, (int(pos[0] + 0.04 * size), int(pos[1] + 0.68 * size), int(0.08 * size), int(0.03 * size)), 0)
    ellipse(surf, brown, (int(pos[0] + 0.18 * size), int(pos[1] + 0.68 * size), int(0.08 * size), int(0.03 * size)), 0)
    rect(surf, dark_brown, (int(pos[0] + 0.05 * size), int(pos[1] + 0.575 * size), int(0.2 * size), int(0.05 * size)),
         0)
    rect(surf, dark_brown, (int(pos[0] + 0.125 * size), int(pos[1] + 0.325 * size), int(0.05 * size), int(0.25 * size)),
         0)

def chukchi_head(surf, size, pos):
    '''
    Drawing head of the chukchi
    param surf: surface to draw on
    param size: scale factor, apply the same head size as chukchi size
    param pos: list of x and y coordinates to place on the surface, apply the same head position as chukchi position
    return: None
    '''
    light_brown = (184, 151, 128)
    face = (214, 196, 194)
    black = (0, 0, 0)
    circle(surf, light_brown, (int(pos[0] + 0.15 * size), int(pos[1] + 0.25 * size)), int(0.075 * size), 0)
    circle(surf, face, (int(pos[0] + 0.15 * size), int(pos[1] + 0.25 * size)), int(0.05 * size), 0)
    aaline(surf, black, (int(pos[0] + 0.11 * size), int(pos[1] + 0.23 * size)),
           (int(pos[0] + 0.13 * size), int(pos[1] + 0.24 * size)))
    aaline(surf, black, (int(pos[0] + 0.16 * size), int(pos[1] + 0.24 * size)),
           (int(pos[0] + 0.183 * size), int(pos[1] + 0.233 * size)))
    arc(surf, black, (int(pos[0] + 0.12 * size), int(pos[1] + 0.27 * size), int(0.06 * size), int(0.04 * size)), 0.5,
        2.5)

def chukchi(surf, size, pos):
    '''
    Drawing one human in particular place with particular size
    param surf: surface to draw on
    param size: Size factor. Note that real with of the body (from hand to hand) is about 0.35*size and real height (from feet to head) is about 0.7*size
    param pos: x and y coordinates of upper-left point of the rectangle in which we're going to draw stuff
    return: None
    '''
    black = (0, 0, 0)

    inclined_hand(surf, size, pos)
    chukchi_body(surf, size, pos)
    chukchi_head(surf, size, pos)
    #and the stick:
    aaline(surf, black, (int(pos[0]), int(pos[1] + 0.2 * size)), (int(pos[0] + 0.03 * size), int(pos[1] + 0.7 * size)))

def igloo(surf, size, pos):
    '''
    draw igloo of particular size in particular place
    param surf: the surface to draw on
    param size: scale factor which is equal to the radius of the half - circle of the igloo
    param pos: coordinates of the center of the half - circle of the igloo
    return: None
    '''
    white = (255, 255, 255)
    black = (0, 0, 0)
    light=(223, 223, 223)
    #shape
    circle(surf, white, pos, size, 0)
    rect(surf, light, (int(pos[0] - size), int(pos[1]), int(2*size), int(size)))
    arc(surf, black, (int(pos[0] - size), int(pos[1] - size), int(2 * size), int(2 * size)), 0, 3.17, 1)
    #bricks
    aaline(surf, black, (int(pos[0] - 0.75 * size), int(pos[1] - 0.66 * size)), (int(pos[0] + 0.75 * size), int(pos[1] - 0.66 * size)))
    aaline(surf, black, (int(pos[0]), int(pos[1] - 0.66 * size)), (int(pos[0]), int(pos[1] - 0.33 * size)))
    aaline(surf, black, (int(pos[0] - 0.94 * size), int(pos[1] - 0.33 * size)), (int(pos[0] + 0.94 * size), int(pos[1] - 0.33 * size)))
    aaline(surf, black, (int(pos[0] - 0.5 * size), int(pos[1] - 0.33 * size)), (int(pos[0] - 0.5 * size), int(pos[1])))
    aaline(surf, black, (int(pos[0] + 0.5 * size), int(pos[1] - 0.33 * size)), (int(pos[0] + 0.5 * size), int(pos[1])))
    aaline(surf, black, (int(pos[0] - size), int(pos[1])), (int(pos[0] + size), int(pos[1])))

def cat_legs_and_tail(surf, size, pos):
    '''
    Drawing cats' four legs and tail as inclined ellipses
    param surf: surface to draw on
    param size: scale factor, apply the same legs size as cat's size for normal proportions
    param pos: x and y coordinates, apply the same legs position as cat's position for normal proportions
    return: None
    '''
    gray = (127, 127, 127)
    light = (223, 223, 223)


    surface = pygame.Surface((int(0.05 * size), int(0.2 * size)))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, int(0.05 * size), int(0.2 * size)), 0)
    surface2 = pygame.transform.rotate(surface, -60)
    surf.blit(surface2, (int(pos[0] + 0.12 * size), int(pos[1] + 0.2 * size)))


    surface = pygame.Surface((int(0.05 * size), int(0.2 * size)))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, int(0.05 * size), int(0.2 * size)), 0)
    surface2 = pygame.transform.rotate(surface, -75)
    surf.blit(surface2, (int(pos[0]), int(pos[1] + 0.15 * size)))

    #tail
    surface = pygame.Surface((int(0.07 * size), int(0.28 * size)))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, int(0.07 * size), int(0.28 * size)), 0)
    surface2 = pygame.transform.rotate(surface, -60)
    surf.blit(surface2, (int(pos[0] + 0.7 * size), int(pos[1] - 0.05 * size)))

    surface = pygame.Surface((int(0.05 * size), int(0.2 * size)))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, int(0.05 * size), int(0.2 * size)), 0)
    surface2 = pygame.transform.rotate(surface, 60)
    surf.blit(surface2, (int(pos[0] + 0.6 * size), int(pos[1] + 0.2 * size)))

def cat_head_and_face(surf, size, pos):
    '''
    Drawing cat's head
    param surf: surface to draw on
    param size: scale factor, apply the same head size as cat's size for normal proportions
    param pos: x and y coordinates, apply the same head position as cat's position for normal proportions
    return: None
    '''
    gray = (127, 127, 127)
    white = (255, 255, 255)
    black = (0, 0, 0)
    light = (223, 223, 223)

    circle(surf, gray, (int(pos[0] + 0.18 * size), int(pos[1] + 0.06 * size)), int(0.08 * size), 0)
    circle(surf, white, (int(pos[0] + 0.16 * size), int(pos[1] + 0.04 * size)), int(0.015 * size), 0)
    circle(surf, white, (int(pos[0] + 0.20 * size), int(pos[1] + 0.05 * size)), int(0.015 * size), 0)
    circle(surf, black, (int(pos[0] + 0.165 * size), int(pos[1] + 0.04 * size)), int(0.005 * size), 0)
    circle(surf, black, (int(pos[0] + 0.205 * size), int(pos[1] + 0.05 * size)), int(0.005 * size), 0)
    polygon(surf, gray, ((int(pos[0] + 0.16 * size), int(pos[1] - 0.02 * size)),
                         (int(pos[0] + 0.19 * size), int(pos[1] - 0.05 * size)),
                         (int(pos[0] + 0.19 * size), int(pos[1] - 0.02 * size))), 0)
    polygon(surf, gray, ((int(pos[0] + 0.20 * size), int(pos[1] - 0.01 * size)),
                         (int(pos[0] + 0.23 * size), int(pos[1] - 0.04 * size)),
                         (int(pos[0] + 0.23 * size), int(pos[1]))), 0)
    polygon(surf, black, ((int(pos[0] + 0.155 * size), int(pos[1] + 0.065 * size)),
                          (int(pos[0] + 0.175 * size), int(pos[1] + 0.065 * size)),
                          (int(pos[0] + 0.165 * size), int(pos[1] + 0.075 * size))), 0)

    surface = pygame.Surface((int(0.05 * size), int(0.2 * size)))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, int(0.05 * size), int(0.2 * size)), 0)
    surface2 = pygame.transform.rotate(surface, 75)
    surf.blit(surface2, (int(pos[0] + 0.7 * size), int(pos[1] + 0.15 * size)))

    ellipse(surf, gray, (int(pos[0] + 0.12 * size), int(pos[1] + 0.08 * size), int(0.66 * size), int(0.15 * size)), 0)

def cat_teeth_and_fish_tail(surf, size, pos):
    '''
    Drawing teeth and fish tail
    param surf: surface to draw on
    param size: scale factor, apply the same size as cat's size for normal proportions
    param pos: x and y coordinates, apply the same position as cat's position for normal proportions
    return: None
    '''
    gray = (127, 127, 127)
    dark_gray = (191, 191, 191)
    white = (255, 255, 255)
    black = (0, 0, 0)

    polygon(surf, dark_gray, [(int(pos[0] + 0.09 * size), int(pos[1] + 0.06 * size)),
                              (int(pos[0] + 0.12 * size), int(pos[1] + 0.12 * size)),
                              (int(pos[0] + 0.22 * size), int(pos[1] + 0.16 * size)),
                              (int(pos[0] + 0.19 * size), int(pos[1] + 0.19 * size)),
                              (int(pos[0] + 0.15 * size), int(pos[1] + 0.09 * size))], 0)
    polygon(surf, black, [(int(pos[0] + 0.09 * size), int(pos[1] + 0.06 * size)),
                          (int(pos[0] + 0.12 * size), int(pos[1] + 0.12 * size)),
                          (int(pos[0] + 0.22 * size), int(pos[1] + 0.16 * size)),
                          (int(pos[0] + 0.19 * size), int(pos[1] + 0.19 * size)),
                          (int(pos[0] + 0.15 * size), int(pos[1] + 0.09 * size))], 1)

    polygon(surf, white, ((int(pos[0] + 0.13 * size), int(pos[1] + 0.08 * size)),
                          (int(pos[0] + 0.14 * size), int(pos[1] + 0.08 * size)),
                          (int(pos[0] + 0.13 * size), int(pos[1] + 0.11 * size))), 0)
    polygon(surf, white, ((int(pos[0] + 0.16 * size), int(pos[1] + 0.095 * size)),
                          (int(pos[0] + 0.17 * size), int(pos[1] + 0.095 * size)),
                          (int(pos[0] + 0.16 * size), int(pos[1] + 0.125 * size))), 0)

def cat(surf, size, pos):
    '''
    Drawing cat of particular size in particular place
    param surf: surface to draw on
    param size: Scale factor. Note that total length of the cat is about 3*size, while total height is about 1.15*size
    param pos: x and y coordinates of upper-left point of the rectangle in which we're going to draw stuff
    return: None
    '''

    cat_legs_and_tail(surf, size, pos)

    cat_head_and_face(surf, size, pos)

    cat_teeth_and_fish_tail(surf, size, pos)

#introducing screen to draw on
screen = pygame.display.set_mode((1024, 640))
screen.fill((255, 255, 255))
rect(screen, (223, 223, 223), (0, 320, 1024, 320), 0)

#drawing picture
draw_picture(screen)

#controlling exit
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()