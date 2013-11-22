#!/usr/bin/env python

import pygame, base, font

from sprites import *
from base import *

ANGLE = 2
SCALE = 1

"""
Create the 'cursor' crosshair
"""
class cursor(gameSprite):
    """
    Set initial position and sprite image, remove system cursor,
    and initialise relevant variables
    """
    def __init__(self, position):
        gameSprite.__init__(self, position)        
        self.sheetimageload('other/gui.png', (0, 0, 32, 32))
        self.rect.center = position
        self.pos = position
        self.clicked = False
        self.action = 'punch'
        self.angle = 0
        self.has_transitioned = False
    
    """
    
    """
    def update(self, position, CLICK):
        self.angle += ANGLE
        if CLICK and not self.clicked and not self.has_transitioned:
            self.transitionClick(position)
        elif CLICK and not self.clicked and self.has_transitioned:
            self.click(position)
        elif not CLICK and self.clicked == True:
            self.sheetimageload('other/gui.png', (0, 0, 32, 32))
            self.clicked = False
            self.has_transitioned = False
        self.rect.center = position
        self.dirty = 1
        self.rotate(self.angle)
    
    """
    
    """
    def click(self, position):
        self.sheetimageload('other/gui.png', (64, 0, 32, 32))
        self.clicked = True
        
    """
    
    """
    def transitionClick(self, position):
        self.sheetimageload('other/gui.png', (32, 0, 32, 32))
        self.has_transitioned = True

class cursortext(gameSprite):
    
    def __init__(self, text, position):
        gameSprite.__init__(self, position)
        self.image = font.gamefont().text(text)
        print self.image
        self.rect.center = position
        
    def update(self, position):
        self.rect.center = (position[0]+20, position[1]-20)
        self.dirty = 1
        
        
        