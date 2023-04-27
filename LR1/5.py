import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Prism import Prism

pygame.init()
display = (900,900)
pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(-2, -2, -10)
glRotatef(90,-1,0,0)

scale = 0
step = 1
i = 0
n=2

change = 0.005
while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          quit()

  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  i += step

  if i<=-100:
    scale = -0.02
    step=1/n
  elif i>=100:
    scale = 0.02
    step = -1/n

  glTranslatef(scale, scale*4, scale)
  Prism(height=3, color=(2, 0.5, 2)).draw()
  pygame.display.flip()
  pygame.time.wait(10)

pygame.quit()
quit()
