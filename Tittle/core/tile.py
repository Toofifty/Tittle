#!/usr/bin/env python

from sprites import gameSprite

TILE_SIZE = 32

"""
Simple tile creator
"""
class tile(gameSprite):
    def __init__(self, x, y, sheet, sheet_pos):
        gameSprite.__init__(self, (x,y))
        gameSprite.sheetimageload(self, 'tile/' + sheet + '.png', sheet_pos)
        
    def update(self):
        self.dirty = 1
