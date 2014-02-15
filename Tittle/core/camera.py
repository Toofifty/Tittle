#! /usr/bin/env python

from pygame.locals import *
import os

WIN_WIDTH = 1280
WIN_HEIGHT = 720
HALF_HEIGHT = WIN_HEIGHT/2

class camera(object):
    def __init__(self, func, width, height):
        self.func = func
        self.state = Rect(0, 0, width, height)
        self.offset = WIN_WIDTH/4
        print('Map size: ' + str(width) + ' x ' + str(height))
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.func(self, target.rect)
        
    def move(self, left, right):
        if right:
            self.offset += 10
            
        if left:
            self.offset -= 10
        
        
# CAMERAS
# 
# l, t are the left and top sides of the target_rect (player)
# w, h are the width and height of the map
# 
# 

"""
Keep the camera centred on the player, wherever
they may go
"""
def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)
        
"""
Keep the camera centred on the player, but stop moving once
hitting the edges of the map
"""
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera.state
    l, t = -l+(camera.offset), -t+HALF_HEIGHT # center player

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.state.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.state.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top

    return Rect(l, t, w, h)
    