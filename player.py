import pygame
from block import Block


class Player:
    def __init__(self, color, position, size):
        self.color = color
        self.position = position
        self.size = size
        self.image = pygame.Surface((size[0]*32, size[1]*32))
        self.image.fill(color)
        self.block = Block(self.image)
