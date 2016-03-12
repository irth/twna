import math
import pygame


class Renderer:
    def __init__(self, world, position, size):
        self.world = world
        self.position = position
        self.size = size

    def render(self):
        surface = pygame.Surface(self.size)
        blocks_x = math.ceil(self.size[0] / 32)+2
        blocks_y = math.ceil(self.size[0] / 32)+2

        if self.position[0] > 0:
            begin_x = math.floor((self.position[0] - 1)/32)
        else:
            begin_x = math.floor((self.position[0])/32)

        if self.position[1] > 0:
            begin_y = math.floor((self.position[1] - 1)/32)
        else:
            begin_y = math.floor((self.position[1])/32)

        if self.position[0] > 0:
            px_x = offset_px_x = -(math.floor((self.position[0] - 1) % 32))
        else:
            px_x = offset_px_x = -(math.floor((self.position[0]) % 32))

        if self.position[1] > 0:
            px_y = offset_px_y = -(math.floor((self.position[1] - 1) % 32))
        else:
            px_y = offset_px_y = -(math.floor(self.position[1] % 32))

        for y in range(0, blocks_y):
            for x in range(0, blocks_x):
                block = self.world.get_at((begin_x+x, begin_y+y))
                surface.blit(block.image, (px_x, px_y))
                px_x += 32
            px_x = offset_px_x
            px_y += 32

        for player in self.world.players:
            surface.blit(
                player.block.image,
                (offset_px_x + player.position[0]*32,
                    offset_px_y + player.position[1]*32 -
                    (player.size[1]*32 - 32)))

        return surface
