#!/usr/bin/env python

import base

from base import *
from tile import tile

class map(object):
    def __init__(self):
        self.map_array = None
    
    def load(self, name):
        self.map_array = base.read('../Tittle/assets/maps/' + name + '_map.txt')
        #with open('../Tittle/assets/maps/' + name + '_map.txt', 'r') as mapfile:
            #self.map_array = mapfile.readlines()
            #for k in range(len(self.map_array)):
            #    self.map_array[k] = self.map_array[k].strip()
        
    def console_print(self):
        for n, line in enumerate(self.map_array, 1):
            print '{:2}.'.format(n), line
        print self.map_array

    def build(self):
        collision_tiles = []
        display_tiles = pygame.sprite.Group()
        x = y = 0
        for row in self.map_array:
            for col in row:
                if col == "P":
                    p = tile(x, y)
                    collision_tiles.append(p)
                    display_tiles.add(p)
                x += 32
            y += 32
            x = 0
        return collision_tiles, display_tiles
    
    def width(self):
        return len(self.map_array[0])*32
    
    def height(self):
        return len(self.map_array)*32