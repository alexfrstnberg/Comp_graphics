import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),
    (1.1, 0.7, 0),
    (1.1, -0.7, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (0, 1, 3),
    (1.1, 0.7, 3),
    (1.1, -0.7, 3),
    (0, -1, 3),
    (-1, 0, 3)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),
    (0, 5),
    (1, 6),
    (2, 7),
    (3, 8),
    (4, 9),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 5)
)

def draw_prism():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -10)

    mouse_pressed = False
    mouse_pos_prev = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pressed = True
                mouse_pos_prev = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pressed = False

        if mouse_pressed:
            mouse_pos = pygame.mouse.get_pos()
            dx = mouse_pos[0] - mouse_pos_prev[0]
            dy = mouse_pos_prev[1] - mouse_pos[1]
            glRotatef(dx, 0, 1, 0)
            glRotatef(dy, 1, 0, 0)
            mouse_pos_prev = mouse_pos

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_prism()
        pygame.display.flip()
        pygame.time.wait(10)

main()
