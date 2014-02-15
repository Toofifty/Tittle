#! /usr/bin/env python


"""
Base file, for simple actions such as loading images
and drawing text, shapes, etc.
"""

import os, pygame, sys, textlogic

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
def rotatecentre(image, angle):
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
def read(source):
    lines = []
    with open(source, 'r') as source:
        for line in source:
            l = line.replace('\n','')
            lines.append(l)
    return lines

"""
Load a sheet into memory, ready to have sprites taken from it
"""
class sheetload(object):
    
    """
    Load the sheet into memory
    """
    def __init__(self, sheet):
        self.sheet = pygame.image.load(SPRITES_FOLDER + sheet).convert_alpha()
        
    """
    Get an image at position rect
    """
    def getimage(self, rect):
        image = self.sheet.subsurface(rect)
        return image
    
    """
    Load a set of images, located at positions in rects
    """
    def getimages(self, rects):
        return [self.getimage(rect) for rect in rects]
    
    """
    Load a strip of images seperately
    """
    def getstrip(self, rect, frames):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(frames)]
        return self.getimages(tups)
    

"""
Load a set of sprite images into an animation, with the next frame
accessible through object.next()
"""
class animload(object):
    
    """
    Initialise the animation and load the strip
    """
    def __init__(self, file, rect, frames, loop = True):
        self.sheet = sheetload(file)
        self.images = self.sheet.getstrip(rect, frames)
        self.i = 0
        self.f = 2
        self.loop = loop
        self.frames = 2
    
    """
    Grab the next frame in the set of images
    """
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                self.i -= 1
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

class pixeltext(object):
    """
    Print pixel text (other/font.png) in-game
    """
    def __init__(self):
        self.font = sheetload('font.png')
        
    def drawtext(self, text, pos):
        rects = textlogic.convertFont(text)
        images = self.font.getimages(rects)
        
        width = 0
        
        for i in images:
            width += i.rect.width
            
        text_box = Rect(pos, (7, width))
        
"""

"""
def imageload(image):
    return pygame.image.load(SPRITES_FOLDER + image).convert_alpha()


def createRectangle(dimensions, colour = None):
    rectangle = pygame.Surface(dimensions).convert()
    if colour is not None:
        rectangle.fill(colour)
    return rectangle
        