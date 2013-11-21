#!/usr/bin/env python

import pygame
import base
from base import *

"""
Basic class for most sprites in the game
"""
class gameSprite(pygame.sprite.DirtySprite):
    
    """
    Initialise the sprite, set its position (in terms of pixels)
    """
    def __init__(self, pixel_position = (0, 0)):
        pygame.sprite.DirtySprite.__init__(self)
        self.x = pixel_position[0]
        self.y = pixel_position[1]
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.center = pixel_position
        self.speed = 0
        
    """
    
    """
    def setup(self):
        pass
    
    """
    Used to translate from tile > pixel coords
    """
    def setTilePosition(self, position):
        pass
    
    """
    Sets a new position for the sprite
    """
    def setPixelPosition(self, position):
        self.pixel_position = position
    
    """
    Gets the next frame for animation strips
    """
    def getNextFrame(self):
        if self.isAnim:
            self.image = self.strips.next()
    
    """
    Set a animation and strip for a sprite
    """
    def setAnim(self, ss, pos, size_mult = 1, loop = True, frames = 8, fps_mult = 1):
        try:
            self.size_mult = size_mult
            self.pos = pos
            self.strips = spriteStripAnim(SPRITES_FOLDER + ss, pos, frames, None, loop, fps_mult * FPS/15)
            self.strips.iter()
            self.image = self.strips
            self.image = pygame.transform.scale(self.strips.next(), (size_mult * pos[2], size_mult * pos[3]))
            _, _, self.rect[2], self.rect[3] = pygame.Rect(self.image.get_rect())
            self.isAnim = True
        except:
            print 'Failure. ' + ss + ': ' + str(pos) + ' is not an animation - ', sys.exc_info()[0]
            raise
            
    """
    Loads a sprite's image from it's own file
    """
    def setSingle(self, image_path, size_mult = 1, angle = None):
        self.image = pygame.image.load(SPRITES_FOLDER + image_path).convert_alpha()
        self.rect = pygame.Rect(self.image.get_rect())
        if not size_mult == 1: 
            self.image = pygame.transform.scale(self.image, (size_mult * self.rect[2], size_mult * self.rect[3]))
        self.src_image = self.image
        if angle:
            self.image = rot_center(self.src_image, angle)
            
            
    """
    Niche method for the occasional sprite that continually rotates
    """
    def rotate(self, angle):
        self.image = rotatecentre(self.src_image, angle)
        return angle

    """
    
    """
    def sheetimageload(self, sheet, pos):
        self.image = base.sheetload(sheet).getimage(pos)
        _, _, self.rect[2], self.rect[3] = pygame.Rect(self.image.get_rect())
        self.src_image = self.image
    
    """
    
    """
    def sheetanimload(self, sheet, pos, frames, loop = True):
        self.strips = animload(sheet, pos, frames, loop)
        self.image = self.strips.next()
        _, _, self.rect[2], self.rect[3] = pygame.Rect(self.image.get_rect())
        self.isAnim = True
        
    """
    
    """
    def imageload(self, image):
        self.image = base.imageload(image)
        