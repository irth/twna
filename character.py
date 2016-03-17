import pygame
from block import Block
from constants import *


class Character:
    def __init__(self, color, position, size):
        self.color = color
        self.position = position
        self.size = size
        self.image = pygame.Surface((size[0]*TILE_SIZE, size[1]*TILE_SIZE))
        self.image.fill(color)
        self.block = Block(self.image)
