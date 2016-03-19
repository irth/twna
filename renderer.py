import math
import pygame
from constants import *


def _px2block(pos):
    (x, y) = pos
    return math.floor(x/TILE_SIZE), math.floor(y/TILE_SIZE)


def _len(a, b):
    return abs(a-b) + 1


class Renderer:
    def __init__(self, world, position, size, player=None):
        self.world = world
        self.position = position
        self.size = size
        self.player = player

    def render(self):
        surface = pygame.Surface(self.size)

        a = _px2block(self.position)
        b = _px2block((self.position[0] + self.size[0] - 1,
                       self.position[1]))
        c = _px2block((self.position[0] + self.size[0] - 1,
                       self.position[1] + self.size[1] - 1))

        (start_x, start_y) = a
        (end_x, end_y) = c

        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                block = self.world.get_at((x, y))
                surface.blit(block.image,
                             ((x-start_x)*TILE_SIZE - self.position[0] % TILE_SIZE,
                              (y-start_y)*TILE_SIZE - self.position[1] % TILE_SIZE))

        for character in self.world.characters:
            (x, y) = character.position
            (w, h) = character.size
            left = self.position[0]/TILE_SIZE - w
            right = (self.position[0] + self.size[0])/TILE_SIZE + w
            top = self.position[1]/TILE_SIZE - 1
            bottom = (self.position[1] + self.size[1])/TILE_SIZE + h - 1

            if left < x < right and top <= y < bottom:
                surface.blit(character.image,
                             ((x - start_x) * TILE_SIZE - self.position[0] % TILE_SIZE,
                              (y - (h - 1) - start_y) * TILE_SIZE - self.position[1] % TILE_SIZE))
        return surface
