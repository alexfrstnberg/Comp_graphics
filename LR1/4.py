import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from Prism import Prism

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
