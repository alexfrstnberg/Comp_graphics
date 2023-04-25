import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from barrel import Barrel, Hexadecagon

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.5, 50.0)
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
        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Barrel(proj='XOY')
        pygame.display.flip()
        pygame.time.wait(10)

main()
