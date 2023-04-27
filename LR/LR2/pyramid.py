from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from itertools import cycle


class Triangle(list):
    def __init__(self, radius=1, x=0, y=0, z=0, color='random'):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.triangle_vertex_coordinates()
        list.__init__(self, self.triangle_vertex_coordinates)

    def construct(self, color='random'):
        glBegin(GL_LINES)
        for vertex in self.triangle_vertices_sequence():
            glColor3fv((0, 1, 0))
            glVertex3fv(vertex)
        glEnd()

    def triangle_vertex_coordinates(self):
        triangle_coordinates = []
        for n in range(3):
            x = self.x + (self.radius*cos(radians(90+n*120)))
            y = self.y + (self.radius*sin(radians(90+n*120)))
            z = self.z
            triangle_coordinates.append([x, y, z])
        self.triangle_vertex_coordinates = triangle_coordinates
        return triangle_coordinates

    def triangle_vertices_sequence(self):
        vertices = self.triangle_vertex_coordinates
        return Triangle.cycled_vertices(vertices)

    def cycled_vertices(vertices):
        duplicated_vertices = [vertex for vertex in vertices for _ in (0, 1)]
        cycled_vertices = []
        cycled = cycle(duplicated_vertices)
        next(cycled)
        for _ in range(len(duplicated_vertices)):
            cycled_vertices.append(next(cycled))

        return cycled_vertices


class Pyramid:
    def __init__(self, radius=1, height=3, x=0, y=0, z=0, color='random'):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height
        self.color = color
        self.base_pyramid_vertices()
        self.pyramid_vertex()

    def construct_pyramid(self):
        self.connect_vertices()

    def base_vertices_sequence(self):
        return self.base_pyramid_vertices.triangle_vertices_sequence()

    def base_vertex_connection_sequence(self):
        base_vertex_connection_sequence = []
        [base_vertex_connection_sequence.extend(
            [vertex, self.pyramid_vertex]) for vertex in self.base_pyramid_vertices]
        return base_vertex_connection_sequence

    def base_pyramid_vertices(self):
        self.base_pyramid_vertices = Triangle(
            self.radius, self.x, self.y, self.z)

    def pyramid_vertex(self):
        self.pyramid_vertex = [self.x, self.y, self.z+self.height]

    def rotate_along_x(self, angle):
        for vertex in self.base_pyramid_vertices:
            Pyramid.rotate_point(vertex, angle, 'x')
        Pyramid.rotate_point(self.pyramid_vertex, angle, 'x')

    def rotate_along_y(self, angle):
        for vertex in self.base_pyramid_vertices:
            Pyramid.rotate_point(vertex, angle, 'y')
        Pyramid.rotate_point(self.pyramid_vertex, angle, 'y')

    def rotate_along_z(self, angle):
        for vertex in self.base_pyramid_vertices:
            Pyramid.rotate_point(vertex, angle, 'z')
        Pyramid.rotate_point(self.pyramid_vertex, angle, 'z')

    def connect_vertices(self):
        glBegin(GL_LINES)

        for vertex in self.base_vertices_sequence():
            glColor3fv((1, 0, 1))
            glVertex3fv(vertex)

        for vertex in self.base_vertex_connection_sequence():
            glColor3fv((0, 1, 0))
            glVertex3fv(vertex)

        glEnd()

    def rotate_point(point, angle, axis):
        angle = radians(angle)
        x, y, z = point
        if axis == 'x':
            point[1] = y*cos(angle) - z*sin(angle)
            point[2] = y*sin(angle) + z*cos(angle)
            #return (x, new_y, new_z)
        elif axis == 'y':
            point[0] = x*cos(angle) + z*sin(angle)
            point[2] = -x*sin(angle) + z*cos(angle)
            #return (new_x, y, new_z)
        elif axis == 'z':
            point[0] = x*cos(angle) - y*sin(angle)
            point[1] = x*sin(angle) + y*cos(angle)
            #return (new_x, new_y, z)
