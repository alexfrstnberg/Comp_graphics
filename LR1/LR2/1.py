import pygame
from pygame.locals import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *

# функція для розрахунку нових координат точок піраміди при обертанні
# Ця функція приймає на вхід координати точки і кут обертання, а повертає нові координати після обертання

def rotate_point(point, angle, axis):
    # кут обертання з градусів в радіани
    angle = radians(angle)
    
    # координати точки
    x, y, z = point
    
    # нові координати після обертання навколо осі X
    if axis == 'x':
        new_y = y*cos(angle) - z*sin(angle)
        new_z = y*sin(angle) + z*cos(angle)
        return (x, new_y, new_z)
    
    # нові координати після обертання навколо осі Y
    elif axis == 'y':
        new_x = x*cos(angle) + z*sin(angle)
        new_z = -x*sin(angle) + z*cos(angle)
        return (new_x, y, new_z)
    
    # нові координати після обертання навколо осі Z
    elif axis == 'z':
        new_x = x*cos(angle) - y*sin(angle)
        new_y = x*sin(angle) + y*cos(angle)
        return (new_x, new_y, z)

# Координати точок трикутної піраміди
pyramid_points = [
    (0, 1, 0),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1)
]

# Індекси точок, які утворюють грані піраміди
pyramid_edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1)
]

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Поюудова граней піраміди
    glBegin(GL_LINES)
    for edge in pyramid_edges:
        for vertex in edge:
            glVertex3fv(pyramid_points[vertex])
    glEnd()

    # Оновлення екрану
    pygame.display.flip()

    # Обертання каркасу навколо осі X
    for i, point in enumerate(pyramid_points):
        new_point = rotate_point(point, 1, 'x')
        pyramid_points[i] = new_point

    # Обертання каркасу навколо осі Y
    for i, point in enumerate(pyramid_points):
        new_point = rotate_point(point, 1, 'y')
        pyramid_points[i] = new_point

    # Обертання каркасу навколо осі Z
    for i, point in enumerate(pyramid_points):
        new_point = rotate_point(point, 1, 'z')
        pyramid_points[i] = new_point

    # Очікування для плавного анімації
    pygame.time.wait(10)

