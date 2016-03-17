import pygame
import os
import json
from block import Block
from character import Character
from constants import *


class World:
    def __init__(self, name, players):
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

            player_count = len(players)

            self.characters = []
            for character in obj['characters']:
                c = Character(character['color'],
                              character['position'],
                              character['size'])
                players[character['player'][player_count-1]-1].characters += [c]
                self.characters += [c]

    def get_at(self, coords):
        try:
            color = self.image.get_at(coords)
        except:
            color = (123, 123, 123)

        if "%s:%s:%s" % color[:3] in self.special_blocks:
            return self.special_blocks["%s:%s:%s" % color[:3]]
        else:
            surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
            surf.fill(color)
            return Block(surf)
