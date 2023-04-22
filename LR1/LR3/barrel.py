import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from random import choice

class Hexadecagon(list):
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        list.__init__(self, self.base_hexadecagon_vertex_coordinates())

    def base_pentagon_vertex_coordinates(self):
        hexadecagon=[]
        for n in range(16):
            x = self.x + (self.radius*math.cos(math.radians(90+n*22.5)))
            y = self.y + (self.radius*math.sin(math.radians(90+n*22.5)))
            z = self.z
            hexadecagon.append([x, y, z])

        return hexadecagon

    def edges_pairs(self):



class Barrel:
    def __init__(self, radius=1, x=0, y=0, z=0, color='random'):
        self.x = x
        self.y = y
        self.z = z
        self.radius = rsdius
        self.height = 3*radius
        self.edges = []
        self.vertices = self.barrel_vertices()
        self.color = color

    def barrel_vertices(self):
        vertices = [] 
        for i in range(5):
            if i == 1 or i == 3:
                radius *= 1.3
            elif i == 2:
                radius *= 1.5
            midpoint = len(vertices) // 2
            z = self.z + self.height // 4 * i

            vertices.insert(midpoint, *Hexadecagon(self.radius, x=self.x, y=self.y, z=z))
            edges.append
        return vertices

    def construct_barrel(self):
        glBegin(GL_LINES)
        for edge in Barrel.all_edges():
            for vertex in edge:
                glColor3fv(self.choose_color(vertex))
                glVertex3fv(self.vertices[vertex])
        glEnd()

