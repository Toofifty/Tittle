#!/usr/bin/env python

import base

from base import *
from tile import tile, TILE_SIZE

class map(object):
    def __init__(self, name):
        self.map_array = None
        self.type = 'Normal'
        self.name = name
        self.load()
    
    def load(self):
        self.map_array = base.read('../Tittle/assets/maps/' + self.name + '_map.txt')
        
    def console_print(self):
        for n, line in enumerate(self.map_array, 1):
            print '{:2}.'.format(n), line
        print self.map_array

    def build(self):
        info = self.info()
        collision_tiles = []
        display_tiles = pygame.sprite.Group()
        x = y = tc = 0
        for set in info:
            for row in self.map_array:
                for col in row:
                    if col == set[0]:
                        t = tile(x, y, set[1], (set[2]*TILE_SIZE, 
                                                set[3]*TILE_SIZE,
                                                TILE_SIZE, 
                                                TILE_SIZE))
                        collision_tiles.append(t)
                        display_tiles.add(t)
                        tc += 1
                    x += 32
                y += 32
                x = 0
            print(str(tc) + " tiles created in set: " + set[0])
            tc = 0
            
        print collision_tiles
        return collision_tiles, display_tiles
    
    def width(self):
        return len(self.map_array[0])*32
    
    def height(self):
        return len(self.map_array)*32
    
    def info(self):
        info = base.read('../Tittle/assets/maps/' + self.name + '_info.txt')
        tile_types = []
        for line in info:
            if '!def ' in line:
                try:
                    line = line.replace('!def ', '')
                    id, loc = line.split(': ', 1)
                    loc = loc.replace(')','')
                    sheet, pos = loc.split('(', 1)
                    pos_x, pos_y = pos.split(',', 1)
                    tile_types.append((id, sheet, int(pos_x), int(pos_y)))
                except:
                    print("Error gathering info")
                    raise SystemExit
            elif 'type: ' in line:
                self.type = line.replace('type: ', '')
        print(tile_types)
        return tile_types
        
        