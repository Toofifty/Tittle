#!/usr/bin/env python

import events
import base

from sprites import *
from base import *

WALK_SPEED = 10
SPRINT_MULT = 1.5

JUMP_HEIGHT = 25

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
        # yvel is a vector pointing downwards
        self.yvel = 0
        # xvel is a vector pointing right
        self.xvel = 0
        
        self.on_ground = False
        self.sheetanimload('player/idle.png', (0, 0, 64, 64), 1, True)
        self.rect[0] = position[0]
        self.rect[1] = position[1]
        print 'Player initialised!'
        self.currentAnim = 'idle'
        self.has_double_jumped = False
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
        # I'm on the ground .: I haven't jumped
        if self.on_ground: 
            self.ready_to_jump = False
            self.has_double_jumped = False
            self.yvel = -vel
            self.start_anim(anim)
            
        # I haven't double jumped yet
        elif not self.has_double_jumped and self.ready_to_jump:
            self.yvel = -vel
            self.start_anim('double' + anim)
            self.has_double_jumped = True
            
        # I've already double jumped
        else:
            pass # slam or something maybe? triple jump?
    
    
    """
    Method for performing certain actions, will be put to use
    later
    """
    def perform_action(self):
        pass
    
    """
    Logic testing for if animation is already started, and sets new anims
    """
    def start_anim(self, anim):
        # Should I start a new anim or continue with mine?
        if not self.currentAnim == anim:
            self.currentAnim = anim
            loop = True # loop is true unless set false
            
            if anim == 'jump':
                frames, loop = 8, False
                
            elif anim == 'jumpl': 
                frames, loop = 8, False
                
            elif anim == 'doublejump': 
                frames, loop = 8, False
                
            elif anim == 'doublejumpl': 
                frames, loop = 8, False
                
            elif anim == 'left': 
                frames = 8
                
            elif anim == 'right': 
                frames = 15
                
            elif anim == 'runningright': 
                frames = 8
                
            elif anim == 'runningleft': 
                frames = 8
                
            elif anim == 'fall': 
                frames = 8        
                       
            elif anim == 'idle': 
                frames = 8
                
            else:
                print anim + ' anim not found for player - ', sys.exc_info()[0]
            
            if frames == 8:
                frames = 1
                
            self.sheetanimload('player/'+ anim +'.png', (0, 0, 96, 128), frames, loop)
            print anim
            
    """
    Method to update the player's position and check collisions
    based on the directions given
    """            
    def update(self, UP, DOWN, LEFT, RIGHT, RUNNING, PLATFORMS):

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
        
        if LEFT and not RUNNING and not RIGHT:
            self.xvel = -WALK_SPEED
            if not UP:
                self.start_anim('left')
            
        if RIGHT and not RUNNING and not LEFT:
            self.xvel = WALK_SPEED
            if not UP:
                self.start_anim('right')
            
        if RUNNING and LEFT and not RIGHT:
            self.xvel = -WALK_SPEED * SPRINT_MULT
            self.start_anim('runningleft')
            
        if RUNNING and RIGHT and not LEFT:
            self.xvel = WALK_SPEED * SPRINT_MULT
            self.start_anim('runningright')
            
        if RIGHT and LEFT:
            self.xvel = 0
            if self.yvel > 0:
                self.start_anim('fall')
                
            else:
                self.start_anim('idle')
        
          
        if not (UP or DOWN or LEFT or RIGHT or RUNNING):
            if self.yvel > 0:
                self.start_anim('fall')
                
            else:
                self.start_anim('idle')
        
        if not self.on_ground:
            self.yvel += 2
            if self.yvel > 100: self.yvel = 100
            
        if not(LEFT or RIGHT):
            self.xvel = 0
            
        self.on_ground = False
        
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, PLATFORMS)
        
        self.rect.top += self.yvel
        self.collide(0, self.yvel, PLATFORMS)
        
        self.getNextFrame()
        self.dirty = 1
    
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
                    self.on_ground = True
                    self.yvel = 0
                    
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
    
"""
Class for creating and initialising a player, possibility
of creating another of these to use as co-op player
"""
class Tittle(Player):
    """
    Initialises Tittle as a player at the given position
    """
    def __init__(self):
        Player.__init__(self, (500, 300))
        
"""
Class for creating and initialising a player, possibility
of creating another of these to use as co-op player
"""
class Tattle(Player):
    """
    Initialises Tittle as a player at the given position
    """
    def __init__(self):
        Player.__init__(self, (500, 300))
        