import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from random import choice
from itertools import cycle


class Hexadecagon(list):
    def __init__(self, radius=1, x=0, y=0, z=0, color="random", proj="None"):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.proj = proj
        list.__init__(self, self.hexadecagon_vertex_coordinates())

    def construct(self, color="random"):
        glBegin(GL_LINES)
        for vertex in self.hexadecagon_vertices():
            glColor3fv((0, 1, 0))
            glVertex3fv(vertex)
        glEnd()

    def hexadecagon_vertex_coordinates(self):
        hexadecagon = []
        for n in range(16):
            x, y, z = [0, 0, 0]
            if self.proj != "YOZ":
                x = self.x + (self.radius * math.cos(math.radians(90 + n * 22.5)))
            if self.proj != "XOZ":
                y = self.y + (self.radius * math.sin(math.radians(90 + n * 22.5)))
            if self.proj != "XOY":
                z = self.z
            hexadecagon.append([x, y, z])
        return hexadecagon

    def hexadecagon_vertices(self):
        vertices = self.hexadecagon_vertex_coordinates()
        return self.cycled_vertices(vertices)

    def cycled_vertices(self, vertices):
        duplicated_vertices = [vertex for vertex in vertices for _ in (0, 1)]
        cycled_vertices = []
        cycled = cycle(duplicated_vertices)
        next(cycled)
        for _ in range(len(duplicated_vertices)):
            cycled_vertices.append(next(cycled))

        return cycled_vertices


class Barrel:
    def __init__(self, radius=1, x=0, y=0, z=0, color="random", proj=None):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = 4 * radius
        self.color = color
        self.proj = proj
        self.construct_barrel()

    def construct_barrel(self):
        vertices = []
        for i in range(6):
            if i == 1 or i == 4:
                radius = 1.3 * self.radius
            elif i == 2 or i == 3:
                radius = 1.4 * self.radius
            else:
                radius = self.radius
            z = self.z + self.height / 6 * i

            hexadecagon = Hexadecagon(radius, self.x, self.y, z, proj=self.proj)
            hexadecagon.construct()

            vertices.extend(hexadecagon)
        self.construct_vertical_edges(vertices)

    def construct_vertical_edges(self, vertices):
        glBegin(GL_LINES)
        for i in range(len(vertices) - 16):
            for vertex in (vertices[i], vertices[i + 16]):
                glColor3fv((1, 0, 1))
                glVertex3fv(vertex)
        glEnd()
