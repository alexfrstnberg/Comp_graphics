#import math
#import pygame
#from pygame.locals import *
#from OpenGL.GL import *
#from OpenGL.GLU import *  
#from Prism import Prism

#def main():
#    pygame.init()
#    display = (1200, 800)
#    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

#    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

#    glTranslatef(0.0, 0.0, -10)
#    glRotatef(80,-1,0,0)

#    x = 0
#    i=0
#    n=2
#    step=1
#    while True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()

#        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # screen flush    
        
#        #i += step

#        #if i <= -100:
#        #    x += 0.01
#        #    step = 1/n
#        #elif i >= 100:
#        #    x -= 0.01
#        #    step = -1/n


#        glTranslatef(x, 0, 0)  # move along x
#        Prism(height=2.5, start=[x,0,0]).draw()

#        x += 0.01
#        if x > 2.0 or x < -2.0:
#            x = 0.0
        

#        pygame.display.flip()
#        pygame.time.wait(10)

#main()


import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from Prism import Prism
vertices = (
    (0, 1, 0),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, -1, 1),
    (1, -1, 1)
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

def draw_pyramid():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

class Pyramid:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        draw_pyramid()
        glPopMatrix()

    def update_position(self, direction, speed):
        if direction == 'right':
            self.y += speed
        elif direction == 'left':
            self.y -= speed

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)
glRotatef(80,-1,0,0)

prism = Prism(height=2.5)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        prism.update_position('left', 0.05)
    if keys[pygame.K_RIGHT]:
        prism.update_position('right', 0.05)
    if keys[pygame.K_UP]:
        prism.update_position('up', 0.05)
    if keys[pygame.K_DOWN]:
        prism.update_position('down', 0.05)




    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    prism.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
