#! /usr/bin/env python

import os
import pygame
import parser
import sprites
import base

from pygame.locals import *
from player import Tittle
from base import *
from tile import *
from cursor import *

"""
Set up screen and some basic variables
"""
ORIGIN = (0, 0)
VIEW_WIDTH = 1280
VIEW_HEIGHT = 720
DIMENSIONS = (VIEW_WIDTH, VIEW_HEIGHT)

screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_icon(pygame.image.load('ico.png').convert_alpha())
pygame.display.set_caption("Tittle's Adventures")


player = None


"""
Starts the game, loads the player and first level (temporary, to
be placed into its own handler)
"""
def startGame(cont = False):
    # initiate global stuff
    global TILES
    global player
    global tiles
    global mouse
    
    TILES = []
    player = Tittle()
    mouse = cursor((VIEW_WIDTH/2, VIEW_HEIGHT/2))
    tiles = pygame.sprite.Group()
    
    # dummy test level
    level = [
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "                                                      ",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    
    # build the level
    x = y = 0
    for row in level:
        for col in row:
            if col == "P":
                p = tile(x, y)
                TILES.append(p)
                tiles.add(p)
            x += 32
        y += 32
        x = 0
        
    # debug to check if we were running
    # this more than once
    print 'New game started!'

class playState:
    
    """
    Define all of the object's variables in the __init__
    """
    def __init__(self):
        self.UP = self.DOWN = self.LEFT = self.RIGHT = self.RUNNING = self.CLICK = False
        print 'PlayState initialised!'
        
    """
    Draw the tiles that are in the array 'tiles'
    """
    def drawTiles(self, tiles):
        for t in tiles:
            screen.blit(t.image, t.rect)
            
    """
    Routine operations happening each tick, from filling the screen to updating
    and drawing new player information
    """
    def execute(self):
        screen.fill(CYAN)
        player.update(self.UP, self.DOWN, self.LEFT, self.RIGHT, self.RUNNING, TILES)
        mouse.update(pygame.mouse.get_pos(), self.CLICK)
        self.drawTiles(tiles)
        screen.blit(player.image, player.rect)
        screen.blit(mouse.image, mouse.rect)
        pygame.display.update()
        
    """
    Handles the input from all sources, and translates to movements or events
    """            
    def handleInput(self):
        
        clock = pygame.time.Clock()
        while True:
            clock.tick(FPS) 
            for e in pygame.event.get():
                if e.type == KEYDOWN and e.type == QUIT: raise SystemExit, "QUIT"
                if e.type == KEYDOWN and e.key == K_ESCAPE: raise SystemExit, "ESCAPE"
                if e.type == KEYDOWN and e.key == K_RETURN: player = Tittle()
                
                if e.type == KEYDOWN and e.key == K_SPACE: self.UP = True
                if e.type == KEYDOWN and e.key == K_s: self.DOWN = True
                if e.type == KEYDOWN and e.key == K_a: self.LEFT = True
                if e.type == KEYDOWN and e.key == K_d: self.RIGHT = True
                if e.type == KEYDOWN and e.key == K_e: self.RUNNING = True
                
                
                if e.type == MOUSEBUTTONDOWN and e.button == 1: self.CLICK = True
                
                if e.type == KEYUP and e.key == K_SPACE: self.UP = False
                if e.type == KEYUP and e.key == K_s: self.DOWN = False
                if e.type == KEYUP and e.key == K_a: self.LEFT = False
                if e.type == KEYUP and e.key == K_d: self.RIGHT = False
                if e.type == KEYUP and e.key == K_e: self.RUNNING = False
                if e.type == MOUSEBUTTONUP and e.button == 1: self.CLICK = False
                    
            self.execute()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        