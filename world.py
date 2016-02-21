import pygame
import os
import json
from block import Block


class World:
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load(
            os.path.join('worlds', name, 'world.png'))
        with open(os.path.join('worlds', name, 'world.json'), 'r') as data:
            obj = json.load(data)
            self.name = obj['name']

            self.assets = {}
            for asset_id in obj['assets']:
                asset = obj['assets'][asset_id]
                if asset['type'] == "image":
                    self.assets[asset_id] = pygame.image.load(
                        os.path.join(
                            'worlds', name, 'images', asset['filename']))

            self.special_blocks = {}
            for block_id in obj['special_blocks']:
                block = obj['special_blocks'][block_id]
                self.special_blocks[block_id] = Block(
                    self.assets[block['image']])

    def get_at(self, coords):
        try:
            color = self.image.get_at(coords)
        except:
            color = (123, 123, 123)

        if "%s:%s:%s" % color[:3] in self.special_blocks:
            return self.special_blocks["%s:%s:%s" % color[:3]]
        else:
            surf = pygame.Surface((32, 32))
            surf.fill(color)
            return Block(surf)
