import sys
import pygame
from pygame.locals import *

from renderer import Renderer
from world import World


pygame.init()

DISPLAYSURF = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Hello World!')

world = World('world1')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    c = Renderer(world, (0, 0), (1024, 768))
    DISPLAYSURF.blit(c.render(), (0, 0))
    pygame.display.update()
