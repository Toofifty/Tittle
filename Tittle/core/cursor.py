#!/usr/bin/env python

import pygame
import base

from sprites import *
from base import *

ANGLE = 2
SCALE = 1

"""
Create the 'cursor' crosshair
"""
class cursor(gameSprite):
    """
    
    """
    def __init__(self, position):
        gameSprite.__init__(self, position)
        self.setSingle('gui/cur_normal.png', SCALE)
        self.rect.center = position
        #pygame.mouse.set_visible(False)
        self.clicked = False
        self.action = 'punch'
        self.angle = 0
        self.has_transitioned = False
    
    """
    
    """
    def update(self, position, CLICK):
        self.rotate(self.angle)
        self.angle += ANGLE
        if CLICK and not self.clicked and not self.has_transitioned:
            self.transitionClick(position)
        elif CLICK and not self.clicked and self.has_transitioned:
            self.click(position)
        elif not CLICK and self.clicked == True:
            self.setSingle('gui/cur_normal.png', SCALE, self.angle)
            self.clicked = False
            self.has_transitioned = False
        self.rect.center = position
    
    """
    
    """
    def click(self, position):
        self.setSingle('gui/cur_small.png', SCALE, self.angle)
        self.clicked = True
        
    """
    
    """
    def transitionClick(self, position):
        self.setSingle('gui/cur_middle.png', SCALE, self.angle)
        self.has_transitioned = True