#! /usr/bin/env python


"""
Base file, for simple actions such as loading images
and drawing text, shapes, etc.
"""

import os, pygame, sys

from pygame.locals import *

# easy colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

ASSETS_FOLDER = 'assets/'
SPRITES_FOLDER = 'assets/sprites/'
MAPS_FOLDER = 'assets/maps/'

FPS = 30
TILE_SIZE = 32
   
"""
Simple text drawer, magically draws cool text
"""
def drawText(source, text, size, colour, shadow = False, copy = False):
    if copy:
        rect = pygame.Surface(source.get_size()).convert()
        rect.blit(source, (0, 0))
    else:
        rect = source
    font = pygame.font.Font(None, size)
    if shadow:
        fontText = font.render(text, 1, BLACK)
        position = fontText.get_rect(centerx = rect.get_width() / 2 + 2, centery = rect.get_height() / 2 + 2)
        rect.blit(fontText, position)
    fontText = font.render(text, 1, colour)
    position = fontText.get_rect(centerx = rect.get_width() / 2, centery = rect.get_height() / 2)
    rect.blit(fontText, position)
    return rect

"""
Rotate an image whilst keeping it's centre and size intact
"""
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

"""
Read text directly from a text file, creating an array with each line
as a value, and line no. as index
"""
def readTxt(source):
    lines = []
    with open(soruce, 'rb') as source:
        for line in source:
            l = line.split('\n')
            lines.append(l)
    return lines

"""
Load a sheet into memory, ready to have sprites taken from it
"""
class sheetload(object):
    
    def __init__(self, sheet):
        self.sheet = pygame.image.load(SPRITES_FOLDER + sheet).convert_alpha()
        
    def getimage(self, rect):
        image = self.sheet.subsurface(rect)
        return image
    
    def getimages(self, rects):
        return [self.getimage(rect) for rect in rects]
    
    def getstrip(self, rect, frames):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(frames)]
        return self.getimages(tups)
    

"""
Load a set of sprite images into an animation, with the next frame
accessible thourgh object.next()
"""
class animload(object):
    
    def __init__(self, file, rect, frames, loop = True):
        self.sheet = sheetload(file)
        self.images = self.sheet.getstrip(rect, frames)
        self.i = 0
        self.f = 2
        self.loop = loop
        self.frames = 2
    
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image