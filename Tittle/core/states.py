#! /usr/bin/env python

# libs
import os, pygame, parser, sprites, base, render, font

# mods
import keyhandler, maploader, settings
from pygame.locals import *
from player import Tittle

# shouldn't really do this
from base import *
from tile import *
from cursor import *
from camera import *


"""
Set up screen and some basic variables
-> 'Read only' globals
These all get processed when 'states' is first called
"""
settings = settings.load()

ORIGIN = (0, 0)
VIEW_WIDTH = settings['screen-width']
VIEW_HEIGHT = settings['screen-height']
DIMENSIONS = (VIEW_WIDTH, VIEW_HEIGHT)

screen = render.init(DIMENSIONS)
pygame.display.set_icon(pygame.image.load('ico.png').convert_alpha())
pygame.display.set_caption("Tittle's Adventures")
background = imageload('background/sky_city.png')


player = None
gfont = font.gamefont()


"""
Starts the game, loads the player and first level (temporary, to
be placed into its own handler)
"""
def startGame(cont = False):
    # startgame should init a new 'playstate' object
    
    # initiate global stuff
    global mouse
    global mtext
    mtext = ''
    
    mouse = cursor((VIEW_WIDTH/2, VIEW_HEIGHT/2))
    mtext = cursortext('Hover text',(VIEW_WIDTH/2, VIEW_HEIGHT/2))
    
    ps = playState('2')
    ps.run()

"""
Handles input, blitting frames and fps
Future: will point to pause menu, home menu, etc
"""
class playState(object):
    
    """
    Define all of the object's variables in the __init__
    """
    def __init__(self, map):
        self.UP = self.DOWN = self.LEFT = self.RIGHT = self.RUNNING = self.CLICK = False
        self.camleft = self.camright = False
        self.scrollup = self.scrolldown = False
        # 'bind' classes to the playstate class, for later use,
        # instead of leaving them floating in the 'global' realm
        self.player = Tittle()
        self.map = maploader.map('2')
        self.TILES, self.tiles = self.map.build()
        self.camera = camera(complex_camera, self.map.width(), self.map.height())

    """
    Draw the tiles that are in the array 'tiles'
    """
    def drawTiles(self):
        for t in self.tiles:
            screen.blit(t.image, self.camera.apply(t))
            
    """
    Routine operations happening each tick, from filling the screen to updating
    and drawing new player information
    """
    def runframe(self):
        screen.blit(background, (0, 0))

        self.camera.move(self.camleft, self.camright)
        self.camera.update(self.player)
        
        self.player.update(self.UP, self.DOWN, self.LEFT, self.RIGHT, self.RUNNING, self.TILES)
        mouse.update(pygame.mouse.get_pos(), self.CLICK)
        if mtext:
            mtext.update(pygame.mouse.get_pos())     
        
        self.drawTiles()
        
        screen.blit(self.player.image, self.camera.apply(self.player))
        screen.blit(mouse.image, mouse.rect)
        if mtext:
            screen.blit(mtext.image, mtext.rect)
        
        pygame.display.update()
        
    """
    Handles the input from all sources, and translates to movements or events
    May be moved to own module
    """            
    def run(self):
        playtime = 0
        clock = pygame.time.Clock()
        
        while True:
            ms = clock.tick(FPS) 
            playtime += ms / 1000.0
            
            action = keyhandler.get_action(self, pygame.event.get())
            if action == 'newplayer':
                del self.player
                self.player = Tittle()
                
            elif action == 'fullscreen':
                render.toggleFullscreen()
                    
            pygame.display.set_caption('FPS: {0:.2f}'.format(clock.get_fps())) 
                    
            self.runframe()
         
"""
Handle pause menus and such
"""   
class MenuState:
    def __init__(self):
        pass