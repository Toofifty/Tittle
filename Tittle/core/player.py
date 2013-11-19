#!/usr/bin/env python

import events
import base

from sprites import *
from base import *

WALK_SPEED = 5
SPRINT_MULT = 1.5

JUMP_HEIGHT = 15
DOUBLE_JUMP_MULT = 1.5

"""
Class to create, spawn and control the player
"""
class Player(gameSprite):
    
    """
    Initialises the player as a gameSprite, a base
    sprite for the game. Sets default velocity variables
    and also sets the sprite to the idle animation
    """
    def __init__(self, position = (0, 0)):
        gameSprite.__init__(self, position)
        self.yvel = 0
        self.xvel = 0
        self.onGround = False
        self.setAnim('player/idle.png', (0, 0, 32, 32), 1, True, 16, False)
        self.rect[0] = position[0]
        self.rect[1] = position[1]
        print self.rect
        print 'Player initialised!'
        self.currentAnim = 'idle'
        self.hasDoubleJumped = False
        self.ready_to_jump = True
        
    """
    Unused
    """
    def setup(self, uid, map, event_bus):
        gameSprite.setup(self, uid, map, event_bus)
        
    """
    
    """
    def getBaseRectTop(self, base_rect_height):
        pass
    
    """
    
    """
    def updateViewRect(self):
        pass       
    
    """
    
    """
    def slide(self, direction):
        pass
    
    """
    
    """
    def sneak(self, direction):
        pass
    
    """
    
    """
    def shoot(self, direction, weapon):
        pass
    
    """
    Processes the jump, at the speed of 'vel'. Performs a double 
    jump if only one jump has occured so far
    """
    def jump(self, vel, anim):
        if self.onGround: 
            self.ready_to_jump = False
            self.hasDoubleJumped = False
            self.yvel -= vel
            # set anim to jump anim
            self.startAnim(anim)
        elif not self.hasDoubleJumped and self.ready_to_jump:
            if self.yvel > 0:
                self.yvel = DOUBLE_JUMP_MULT*vel * -self.yvel / 2
                if self.yvel < -20:
                    self.yvel = -20
            elif self.yvel < 0:
                self.yvel = -vel
            # set anim to jump anim
            self.startAnim('double' + anim)
            self.hasDoubleJumped = True
            #print 'double jump!'
        else:
            pass # slam or something maybe? triple jump?
    
    """
    Method for performing certain actions, will be put to use
    later
    """
    def performAction(self):
        pass
    """
    
    """
    def startAnim(self, anim):
        if not self.currentAnim == anim:
            self.currentAnim = anim
            loop = True
            flip = False
            fps = 1
            if anim == 'jump':
                start, frames, loop = (0, 64), 16, False
            elif anim == 'jumpl':
                start, frames, loop, flip = (0, 64), 16, False, True
            elif anim == 'doublejump':
                start, frames, loop = (0, 96), 8, False
            elif anim == 'doublejumpl':
                start, frames, loop, flip = (0, 96), 8, False, True  # temp? 
            elif anim == 'left':
                start, frames, flip = (0, 32), 8, True # temp?
            elif anim == 'right':
                start, frames = (0, 32), 8
            elif anim == 'runningright':
                start, frames = (0, 0), 8 # temp
            elif anim == 'runningleft':
                start, frames, flip = (0, 0), 8, True # temp
            elif anim == 'fall':
                start, frames, flip = (0, 0), 8, True # temp                
            else: #idle
                start, frames, fps = (0, 0), 16, 1
            self.setAnim('player/'+ anim +'.png', (start[0], start[1], 32, 32), 1, loop, frames, flip, fps)
            print anim
    """
    Method to update the player's position and check collisions
    based on the directions given
    """            
    def update(self, UP, DOWN, LEFT, RIGHT, RUNNING, PLATFORMS):
        # print self.ready_to_jump
        
        if UP and self.ready_to_jump: 
            if LEFT:
                self.jump(JUMP_HEIGHT, 'jumpl')
            else:
                self.jump(JUMP_HEIGHT, 'jump')                
            self.idling = False
            
        if not UP:
            self.ready_to_jump = True
            
        if DOWN:
            pass
        
        if LEFT:
            self.xvel = -WALK_SPEED
            if not UP:
                self.startAnim('left')
            
        if RIGHT:
            self.xvel = WALK_SPEED
            if not UP:
                self.startAnim('right')
            
        if RUNNING and LEFT:
            self.xvel = -WALK_SPEED * SPRINT_MULT
            self.startAnim('runningleft')
            
        if RUNNING and RIGHT:
            self.xvel = WALK_SPEED * SPRINT_MULT
            self.startAnim('runningright')
            
        if RIGHT and LEFT:
            self.xvel = 0
            if self.yvel > 0:
                self.startAnim('fall')
            else:
                self.startAnim('idle')
        
          
        if not (UP or DOWN or LEFT or RIGHT or RUNNING):
            if self.yvel > 0:
                self.startAnim('fall')
            else:
                self.startAnim('idle')
        
        if not self.onGround:
            self.yvel += 1
            if self.yvel > 100: self.yvel = 100
            
        if not(LEFT or RIGHT):
            self.xvel = 0
            
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, PLATFORMS)
        self.rect.top += self.yvel
        self.onGround = False
        self.collide(0, self.yvel, PLATFORMS)  
        self.getNextFrame()
        #self.rotate(10)
        #print RUNNING
        #print self.xvel
    
    """
    Places the player at a certain position after
    colliding with an object
    """
    def collide(self, xvel, yvel, PLATFORMS):
        for p in PLATFORMS:      
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "right collide"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "left collide"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
    
"""
Class for creating and initialising a player, possibility
of creating another of these to use as co-op player
"""
class Tittle(Player):
    """
    Initialises Tittle as a player at the given position
    """
    def __init__(self):
        Player.__init__(self, (50, 50))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        