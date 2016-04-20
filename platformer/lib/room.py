import math

import pygame

import graphics
import tile

max_x = graphics.screen_w
max_y = graphics.screen_h
rows = graphics.screen_h / tile.height
cols = graphics.screen_w / tile.width

def load(file_in):
    file_descriptor = open(file_in)
    lines = file_descriptor.readlines()
    file_descriptor.close()

    tiles = []
    for c in range(cols):
        tiles.append([])
        for r in range(rows):
            tiles[c].append(tile.tile[lines[r][c]])

    exit_lines = lines[rows:]
    exits = {}
    for line in exit_lines:
        direction, file_name = line.strip().split(":")
        exits[direction] = file_name
        
    print exits

    return Room(tiles, exits)


class Room(object):
    def __init__(self, tiles, exits):
        self.tiles = tiles
        self.exits = exits

    def draw(self, surface):
        for x in range(cols):
            for y in range(rows):
                surface.blit(self.tiles[x][y].surface, (x*tile.width, y*tile.height))

    def tiles_around(self, (x, y)):
        t_x = int(math.floor(x / tile.width))
        t_y = int(math.floor(y / tile.width))
        tiles = []
        for x in range(t_x-1, t_x+2):
            tiles.append([])
            for y in range(t_y-1, t_y+2):
                if 0 <= x < cols and 0 <= y < rows:
                    rect = pygame.rect.Rect(x*tile.width, y*tile.height, tile.width, tile.height)
                    tiles[-1].append((rect, self.tiles[x][y]))
                else:
                    print x, t_x
                    tiles[-1].append(None)
        return tiles

    def rect_at(self, (x, y)):
        t_x = int(math.floor(x / tile.width))
        t_y = int(math.floor(y / tile.height))
        return pygame.rect.Rect((t_x * tile.width, t_y * tile.height),\
                                (tile.width, tile.height))

    def solid_at(self, (x, y)):
        x = int(math.floor(x / tile.width))
        y = int(math.floor(y / tile.height))
        if not (0 <= x < cols):
            return True
        if not (0 <= y < rows):
            return True
        return self.tiles[x][y].solid

    def write_info(self, (x, y)):
        x = int(math.floor(x / tile.width))
        y = int(math.floor(y / tile.height))
        t = self.tiles[x][y]
        print "Coordinates: {0}, {1} - Tile: {2} - Solid: {3}".format(x, y, t.name, t.solid)

