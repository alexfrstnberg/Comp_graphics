import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 0, 0),
    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 0, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 7),
    (5, 6),
    (6, 7),
)

faces = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (5, 6, 2, 1),
    (7, 4, 0, 3),
)

def barrel():
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    for edge in edges:
        # Розбиваємо ребра на 6 частин та з'єднуємо їх між собою під кутом
        x1, y1, z1 = vertices[edge[0]]
        x2, y2, z2 = vertices[edge[1]]
        dx = (x2 - x1) / 6.0
        dy = (y2 - y1) / 6.0
        dz = (z2 - z1) / 6.0
        for i in range(6):
            glVertex3f(x1 + i * dx, y1 + i * dy, z1 + i * dz)
            glVertex3f(x1 + (i + 1) * dx, y1 + (i + 1) * dy, z1 + (i + 1) * dz)
            glVertex3f(x1 + (i + 1) * dx, y1 + (i + 1) * dy, z1 + (i + 1) * dz + 0.1)
            glVertex3f(x1 + i * dx, y1 + i * dy, z1 + i * dz + 0.1)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)


        glTranslatef(0.0,0.0,-5)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            barrel()
            pygame.display.flip()
            pygame.time.wait(10)

main()
