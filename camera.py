import math
import pygame

class Camera:
    def __init__(self, world, position, size):
        self.world = world
        self.position = position
        self.size = size

    def render(self):
        surface = pygame.Surface(self.size)
        blocks_x = math.ceil(self.size[0] / 32)+2
        blocks_y = math.ceil(self.size[0] / 32)+2
        begin_x = math.floor((self.position[0] - 1)/32) if self.position[0] > 0 else math.floor((self.position[0])/32)
        begin_y = math.floor((self.position[1] - 1)/32) if self.position[1] > 0 else math.floor((self.position[1])/32)

        px_x = initial_px_x = -(math.floor((self.position[0] - 1)%32) if self.position[0] > 0 else math.floor(self.position[0])%32)
        px_y = -(math.floor((self.position[1] - 1)%32) if self.position[1] > 0 else math.floor(self.position[1]%32))
        print(px_y)
        for y in range(0, blocks_y):
            for x in range(0, blocks_x):
                block = self.world.get_at((begin_x+x,begin_y+y));
                surface.blit(block.image, (px_x, px_y))
                px_x += 32
            px_x = initial_px_x
            px_y += 32
        return surface


