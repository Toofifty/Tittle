#!/usr/bin/env python

import pygame

from sprites import *
from pygame import *
from base import *

"""
Simple tile creator
"""
class tile(gameSprite):
    def __init__(self, x, y):
        gameSprite.__init__(self, (x,y))
        gameSprite.sheetimageload(self, 'tile/static.png', (32, 0, 32, 32))
        
    def update(self):
        self.dirty = 1
