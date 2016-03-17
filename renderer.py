import math
import pygame


def _px2block(pos):
    (x, y) = pos
    return math.floor(x/32), math.floor(y/32)


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
                             ((x-start_x)*32 - self.position[0] % 32,
                              (y-start_y)*32 - self.position[1] % 32))

        # TODO: draw characters

        return surface
