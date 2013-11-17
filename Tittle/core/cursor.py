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
    Set initial position and sprite image, remove system cursor,
    and initialise relevant variables
    """
    def __init__(self, position):
        gameSprite.__init__(self, position)
        #self.setSingle('gui/cur_normal.png', SCALE)
        # no longer needs it's own file
        self.setTexture('gui_sheet.png', (0, 0, 32, 32))
        self.rect.center = position
        pygame.mouse.set_visible(False)
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
            #self.setSingle('gui/cur_normal.png', SCALE, self.angle)
            # no longer needs own file
            self.setTexture('gui_sheet.png', (0, 0, 32, 32)) # normal size cursor
            self.clicked = False
            self.has_transitioned = False
        self.rect.center = position
    
    """
    
    """
    def click(self, position):
        # no longer needs own file
        self.setTexture('gui_sheet.png', (64, 0, 32, 32)) # small size cursor
        self.clicked = True
        
    """
    
    """
    def transitionClick(self, position):
        # no longer needs own file
        self.setTexture('gui_sheet.png', (32, 0, 32, 32)) # med size cursor
        #self.setSingle('gui/cur_middle.png', SCALE, self.angle)
        self.has_transitioned = True