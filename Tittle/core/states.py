#! /usr/bin/env python

import os, pygame, parser, sprites, base, render
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

screen = render.init(DIMENSIONS)
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
    global allsprites
    
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
        
    allsprites = pygame.sprite.LayeredDirty((player, mouse))
        
    # debug to check if we were running
    # this more than once
    print 'New game started!'

"""
Handles input, blitting frames and fps
Future: will point to pause menu, home menu, etc
"""
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
            #screen.blit(t.image, t.rect)
            allsprites.add(t)
            
    """
    Routine operations happening each tick, from filling the screen to updating
    and drawing new player information
    """
    def execute(self):
        
        player.update(self.UP, self.DOWN, self.LEFT, self.RIGHT, self.RUNNING, TILES)
        mouse.update(pygame.mouse.get_pos(), self.CLICK)
        
        self.drawTiles(tiles)
        
        #screen.blit(player.image, player.rect)
        #render.dirty(player.rect)
        #screen.blit(mouse.image, mouse.rect)
        #render.dirty(mouse.rect)
        screen.fill(CYAN)
        rects = allsprites.draw(screen)
        pygame.display.update(rects)
        
        #render.update()
        
    """
    Handles the input from all sources, and translates to movements or events
    May be moved to own module
    """            
    def handleInput(self):
        playtime = 0
        clock = pygame.time.Clock()
        while True:
            ms = clock.tick(FPS) 
            playtime += ms / 1000.0
            for e in pygame.event.get():
                if e.type == KEYDOWN and e.type == QUIT: raise SystemExit, "QUIT"
                if e.type == KEYDOWN and e.key == K_ESCAPE: raise SystemExit, "ESCAPE"
                if e.type == KEYDOWN and e.key == K_RETURN: player = Tittle()
                
                if e.type == KEYDOWN and e.key == K_SPACE: self.UP = True
                if e.type == KEYDOWN and e.key == K_s: self.DOWN = True
                if e.type == KEYDOWN and e.key == K_a: self.LEFT = True
                if e.type == KEYDOWN and e.key == K_d: self.RIGHT = True
                if e.type == KEYDOWN and e.key == K_LSHIFT: self.RUNNING = True
                if e.type == KEYDOWN and e.key == K_F11: render.toggleFullscreen()
                
                
                if e.type == MOUSEBUTTONDOWN and e.button == 1: self.CLICK = True
                
                if e.type == KEYUP and e.key == K_SPACE: self.UP = False
                if e.type == KEYUP and e.key == K_s: self.DOWN = False
                if e.type == KEYUP and e.key == K_a: self.LEFT = False
                if e.type == KEYUP and e.key == K_d: self.RIGHT = False
                if e.type == KEYUP and e.key == K_LSHIFT: self.RUNNING = False
                if e.type == MOUSEBUTTONUP and e.button == 1: self.CLICK = False
                    
            pygame.display.set_caption('FPS: {0:.2f}'.format(clock.get_fps())) 
                    
            self.execute()
            