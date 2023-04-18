import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Pentagon(list):
    def __init__(self, radius=1, start=[0,0,0]):
        self.radius = radius
        self.start = start
        list.__init__(self, self.base_pentagon_vertex_coordinates())

    def base_pentagon_vertex_coordinates(self):
        pentagon=[]
        for n in range(0,5):
            x = self.start[0] + (self.radius*math.cos(math.radians(90+n*72)))
            y = self.start[1] + (self.radius*math.sin(math.radians(90+n*72)))
            z = self.start[2]
            pentagon.append([x, y, z])

        return pentagon

class Prism:
    def __init__(self, radius=1, height=1, start=[0,0,0], color=(1,0,0)):
        self.vertices = Prism.prism_vertices(radius, height, start)
        self.color = color

    def draw(self):
        #glEnable(GL_LINE_STIPPLE)
        #glLineStipple(3, 0x0F0F)
        #glColor3fv(self.color)
        #glBegin(GL_LINES)
        #for edge in Prism.invisible_edges():
        #    for vertex in edge:
        #        glVertex3fv(self.vertices[vertex])
        #glEnd()

        glDisable(GL_LINE_STIPPLE)
        glColor3fv(self.color)
        glBegin(GL_LINES)
        for edge in Prism.all_edges():
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def all_edges():
        return ((0,1), (1,2), (4,0), (0,5), (1,6), (2,3), (3,4), (2,7), (3,8), (4,9), (5,6), (6,7), (7,8), (8,9), (9,5))

    def visible_edges():
        return ((2,3), (3,4), (2,7), (3,8), (4,9), (5,6), (6,7), (7,8), (8,9), (9,5))

    def invisible_edges():
        return ((0,1), (1,2), (4,0), (0,5), (1,6))

    def prism_vertices(radius=1, height=1, start=[0,0,0]):
        base_pentagon = Pentagon(radius, start)
        upper_start = start[:]
        upper_start[2] = height
        upper_pentagon = Pentagon(radius, upper_start)

        return base_pentagon + upper_pentagon
