import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from random import choice

class Pentagon(list):
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        list.__init__(self, self.base_pentagon_vertex_coordinates())

    def base_pentagon_vertex_coordinates(self):
        pentagon=[]
        for n in range(0,5):
            x = self.x + (self.radius*math.cos(math.radians(90+n*72)))
            y = self.y + (self.radius*math.sin(math.radians(90+n*72)))
            z = self.z
            pentagon.append([x, y, z])

        return pentagon

class Prism:
    COLORS = [
    (1, 0, 0),
    (2, 0.5, 2),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (2, 0.5, 2),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (2, 0.5, 2),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0)
]
    def __init__(self, radius=1, height=1, x=0, y=0, z=0, color='random'):
        self.x = x
        self.y = y
        self.z = z
        self.vertices = self.prism_vertices(radius, height)
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
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)

        self.construct_prism()

        glPopMatrix()

    def choose_color(self, vertex):
        if self.color == 'random':
           return self.COLORS[vertex]
        else:
            return self.color

    def construct_prism(self):
        glBegin(GL_LINES)
        for edge in Prism.all_edges():
            for vertex in edge:
                glColor3fv(self.choose_color(vertex))
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def update_position(self, direction, speed):
      if direction == 'right':
        self.x += speed
      elif direction == 'left':
        self.x -= speed
      elif direction == 'up':
        self.y += speed
      elif direction == 'down':
        self.y -= speed

    def prism_vertices(self, radius=1, height=1):
        base_pentagon = Pentagon(radius, x=self.x, y=self.y, z=self.z)
        z = self.z + height
        upper_pentagon = Pentagon(radius, x=self.x, y=self.y, z=z)

        return base_pentagon + upper_pentagon

    def all_edges():
        return ((0,1), (1,2), (4,0), (0,5), (1,6), (2,3), (3,4), (2,7), (3,8), (4,9), (5,6), (6,7), (7,8), (8,9), (9,5))

    def visible_edges():
        return ((2,3), (3,4), (2,7), (3,8), (4,9), (5,6), (6,7), (7,8), (8,9), (9,5))

    def invisible_edges():
        return ((0,1), (1,2), (4,0), (0,5), (1,6))

