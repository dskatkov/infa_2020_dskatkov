import pygame
import numpy
from pygame.draw import *
from random import randint

pygame.init()

# setting FPS and screen size
FPS = 25
screen = pygame.display.set_mode((1200, 900))

# coloring
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# defining way too many functions
def new_ball():
    '''
    function creates a new ball on a screen
    :return: moving ball on a pygame surface
    '''
    x = randint(100, 1200)
    y = randint(100, 900)
    r = randint(30, 50)
    velocityX = randint(-10, 10)
    velocityY = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    lifetime = 0
    return [x, y, r, color, False, velocityX, velocityY, lifetime]


def catch_checker(event, ball_coordinates):
    '''
    function checks whether you've hit the ball or cockroach or not
    :param event: event which check is based on
    :param ball_coordinates: position of the ball on a screen
    :return: 1 if you hit a ball, 2 if you hit a cockroach, 0 otherwise
    '''
    for i in ball_coordinates:
        x, y, r = i[0], i[1], i[2]
        ball_is_touched = i[4]
        distanse_to_the_ball_center_squared = (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2
        if distanse_to_the_ball_center_squared <= r ** 2 and not ball_is_touched:
            i[4] = True
            return True
    return False


def strike_wall(current_ball):
    '''
    function changes ball's velocity if it hits the wall
    :param current_ball: the ball which is under consideration
    :return: ball of changed velocity receding from the wall
    '''
    if current_ball[0] < 0 or current_ball[0] > 1200:
        current_ball[5] *= -1
    if current_ball[1] < 0 or current_ball[1] > 900:
        current_ball[6] *= -1


def new_cockroach():
    '''
    function creates a new cockroach on the screen
    :return: a new cockroach moving on a surface
    '''
    x = randint(100, 700)
    y = randint(100, 500)
    size = randint(20, 40)
    velocityX = randint(-20, 20)
    velocityY = randint(-20, 20)
    color = (206, 134, 31)
    lifetime = 0
    return [x, y, size, color, False, velocityX, velocityY, lifetime]


def cockroach_checker(event, cockroaches):
    '''
    function
    :param event:
    :param cockroaches:
    :return:
    '''
    for cockroach in cockroaches:
        x, y, r = cockroach[0], cockroach[1], cockroach[2]
        is_touched = cockroach[4]
        if (x - event.pos[0]) ** 2 <= r ** 2 and 4 * (y - event.pos[1]) ** 2 <= r ** 2 and not is_touched:
            cockroach[4] = True
            cockroach[3] = (156, 84, 11)
            return True
    return False


def draw_cockroach(surf, cockroach):
    '''
    the function rotates the cockroach and puts it on the screen
    :param surf: the surface on which the cockroach is put
    :param cockroach: the cockroach put on the surface
    :return: a rotated cockroach on a given pygame surface
    '''
    x, y, r, Vx, Vy = cockroach[0], cockroach[1], cockroach[2], cockroach[5], cockroach[5]
    surface = pygame.Surface((r, r))
    surface.fill((0, 0, 0))
    ellipse(surface, cockroach[3], (0, 0, r, r // 2))
    line(surface, (0, 0, 0), (0, r // 4), (3 * r // 4, r // 4), 2)
    line(surface, (0, 0, 0), (3 * r // 4, 0), (3 * r // 4, r // 2), 2)
    surface.set_colorkey(BLACK)
    angle = 57 * numpy.arctan(Vy / (Vx + 0.01))
    if Vx * Vy > 0:
        angle += 90
    surface2 = pygame.transform.rotate(surface, angle)
    surf.blit(surface2, (x, y))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
phase = 0

# initial balls and cockroaches lists setting
ball_coordinates = [new_ball()]
cockroaches = [new_cockroach()]

# processing events
while not finished:
    clock.tick(FPS)
    # filling screen with living balls
    for cockroach in cockroaches:
        if cockroach[4]:
            circle(screen, cockroach[3], (cockroach[0], cockroach[1]), cockroach[2])
    for ball in ball_coordinates:
        ball[7] += 1
        if ball[7] % 20 == 0:
            ball[2] -= 1
        if ball[2] == 0:
            ball[4] = True
        if not ball[4]:
            ball[0] += ball[5]
            ball[1] += ball[6]
            strike_wall(ball)
            circle(screen, ball[3], (ball[0], ball[1]), ball[2])
    for cockroach in cockroaches:
        if not cockroach[4]:
            cockroach[0] += cockroach[5]
            cockroach[1] += cockroach[6]
            cockroach[5] += randint(-2, 2)
            cockroach[6] += randint(-2, 2)
            strike_wall(cockroach)
            draw_cockroach(screen, cockroach)
    # filing space with cockroaches
    # events controller
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if catch_checker(event, ball_coordinates):
                score += 1
            if cockroach_checker(event, cockroaches):
                score += 2
    # new items generation
    phase += 1
    if phase % 10 == 0:
        ball_coordinates.append(new_ball())
    if phase % 100 == 0:
        cockroaches.append(new_cockroach())
    # screen updating
    pygame.display.update()
    screen.fill(BLACK)

# the end of the game
print('score =', score)
pygame.quit()
