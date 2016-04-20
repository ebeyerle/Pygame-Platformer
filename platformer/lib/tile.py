import os

import pygame

tile = {}

height = 32
width = 32
size = (width, height)

image_path = os.path.join("data", "tiles")

tile_info = {
#   code: (name,    solid,  image_file)
    ' ' : ('empty', False, 'empty.png'),
    '#' : ('brick wall', True, 'brick wall.png'),
    'D' : ('dirt wall', True, 'dirt wall.png'),
    'W' : ('rightwall', True, 'rightwall.png'),
    'T' : ('topscreen', True, 'topscreen.png'),
    'L' : ('corner', True, 'corner.png'),
    'C' : ('rightcorner', True, 'rightcorner.png'),
    'P' : ('topleftcorner', True, 'topleftcorner.png'),
    'A' : ('toprightcorner', True, 'toprightcorner.png')
}

class Tile(object):
    def __init__(self, name, solid, surface):
        self.name = name 
        self.solid = solid
        self.surface = surface


def init():
    #Tile information
    global tile
    for t in tile_info.keys():
        name = tile_info[t][0]
        solid = tile_info[t][1]
        surface = pygame.image.load(tile_info[t][2]).convert()
        tile[t] = Tile(name, solid, surface)

