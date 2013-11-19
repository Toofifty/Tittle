#!/usr/bin/env python

import sys, pygame
from pygame.locals import Rect, FULLSCREEN, HWSURFACE, RLEACCEL

surface = None
rect = Rect(0, 0, 0, 0)
dirtyrects = []
fs = 0

def init(size, fullscreen = 0):
    global screen, rect
    try:
        flags = 0
        if fullscreen:
            flags |= FULLSCREEN
        screen = pygame.display.set_mode(size, flags)
        rect = screen.get_rect()
        
        pygame.mouse.set_visible(False)
        
        return screen
    except pygame.error, msg:
        raise pygame.error, 'Cannot initialise render engine ' + str(msg)
    
def toggleFullscreen():
    global fs
    if fs:
        fs = 0
        pygame.display.set_mode(screen.get_size(), FULLSCREEN)
    else:
        fs = 1
        pygame.display.set_mode(screen.get_size())
    
def dirty(rect):
    dirtyrects.append(rect)
    
def update():
    global dirtyrects
    pygame.display.update(dirtyrects)
    del dirtyrects [:]