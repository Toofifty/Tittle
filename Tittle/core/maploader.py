#!/usr/bin/env python

import base
import traceback

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
        for row in self.map_array:
            for col in row:
                if col != " ":
                    t = tile(x, y,
                             info[col][0],
                             (info[col][1]*TILE_SIZE, 
                                            info[col][2]*TILE_SIZE,
                                            TILE_SIZE, 
                                            TILE_SIZE))
                    if info[col][3]:
                        collision_tiles.append(t)
                    display_tiles.add(t)
                    tc += 1
                x += 32
            y += 32
            x = 0
        return collision_tiles, display_tiles
    
    def width(self):
        return len(self.map_array[0])*32
    
    def height(self):
        return len(self.map_array)*32
    
    def info(self):
        info = base.read('../Tittle/assets/maps/' + self.name + '_info.txt')
        tile_types = {}
        for line in info:
            if '!def ' in line:
                try:
                    if ' ^' in line:
                        line = line.replace('!def ^','')
                        clip = False
                    else:
                        line = line.replace('!def ', '')
                        clip = True
                    id, loc = line.split(': ', 1)
                    loc = loc.replace(')','')
                    sheet, pos = loc.split('(', 1)
                    pos_x, pos_y = pos.split(',', 1)
                    tile_types.setdefault(id,[])
                    tile_types[id].append(sheet)
                    tile_types[id].append(int(pos_x))
                    tile_types[id].append(int(pos_y))
                    tile_types[id].append(clip)
                except:
                    print("Error gathering info")
                    traceback.print_exc()
                    raise SystemExit
            elif 'type: ' in line:
                self.type = line.replace('type: ', '')
        print(tile_types)
        return tile_types
        
        