#! /usr/bin/env python

from pygame.locals import *

WIN_WIDTH = 1280
WIN_HEIGHT = 720
HALF_WIDTH = WIN_WIDTH/2
HALF_HEIGHT = WIN_HEIGHT/2

class camera(object):
    def __init__(self, func, width, height):
        self.func = func
        self.state = Rect(0, 0, width, height)
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.func(self.state, target.rect)
        
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h # center player

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top

    return Rect(l, t, w, h)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)