#!/usr/bin/env python

import sys, pygame
from pygame.locals import Rect, FULLSCREEN, HWSURFACE, RLEACCEL

surface = None
rect = Rect(0, 0, 0, 0)
dirtyrects = []
fs = 0

"""
Initialise the screen, fullscreen if needed
"""
def init(size, fullscreen = 0):
    global screen, rect
    try:
        flags = 0
        if fullscreen:
            flags |= FULLSCREEN
        screen = pygame.display.set_mode(size, flags)
        rect = screen.get_rect()
        
        pygame.mouse.set_visible(False)
        pygame.display.update()
        return screen
    except pygame.error, msg:
        raise pygame.error, 'Cannot initialise render engine ' + str(msg)

"""
Toggles between fullscreen and windowed
Pixel scaling isn't quite right, should fix
"""
def toggleFullscreen():
    global fs
    if fs:
        fs = 0
        pygame.display.set_mode(screen.get_size(), FULLSCREEN)
    else:
        fs = 1
        pygame.display.set_mode(screen.get_size())
    
"""
Add a rect to the list of dirty rects
"""
def dirty(rect):
    dirtyrects.append(rect)
    
"""
Update all dirty rects blitted, nothing else
Need to make it update all old rects as well
"""
def update():
    global dirtyrects
    pygame.display.update(dirtyrects)
    del dirtyrects [:]
