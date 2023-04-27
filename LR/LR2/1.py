import pygame
from pygame.locals import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pyramid import Pyramid

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.5, 50.0)
glTranslatef(0.0, 0.0, -10)
glRotatef(45,-1,0,0)
pyramid = Pyramid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    pyramid.construct_pyramid()
    pygame.display.flip()
    pyramid.rotate_along_x(1)
    pyramid.rotate_along_y(1)
    pyramid.rotate_along_z(1)
    pygame.time.wait(10)

