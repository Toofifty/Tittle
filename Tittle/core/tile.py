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
        gameSprite.setTexture(self, 'tile/static.png', (0, 0, 32, 32), 1)
        
    def update(self):
        pass
