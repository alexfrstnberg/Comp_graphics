import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *  
from Prism import Prism

def main():
    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -10)
    glRotatef(80,-1,0,0)

    t = 0
    scale = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        x = 5 * math.cos(t)
        y = 2 * math.sin(t)
        z = 0

        glTranslatef(x, y, z)
        glScalef(scale, scale, scale)
        Prism(height=2.5, start=[0,0,-2]).draw()
        glPopMatrix()

        t += 0.02
        scale = 0.5 * math.sin(t) + 1

        pygame.display.flip()
        pygame.time.wait(10)

main()