import sys
import pygame
from pygame.locals import *

from renderer import Renderer
from player import Player
from world import World


pygame.init()

DISPLAYSURF = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Hello World!')

player = Player("bob")
world = World('world1', [player])

c = Renderer(world, (0, 0), (1024, 768), player)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(c.render(), (0, 0))
    pygame.display.update()
