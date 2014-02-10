#! /usr/bin/env python

# libs
import os, pygame, parser, sprites, base, render, font

# mods
import keyhandler
import settings
from pygame.locals import *
from player import Tittle

# possibly bad practice
from base import *
from tile import *
from cursor import *
from camera import *
from maploader import map


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
    
    player = Tittle()
    mouse = cursor((VIEW_WIDTH/2, VIEW_HEIGHT/2))
    #mtext = cursortext('Test text',(VIEW_WIDTH/2, VIEW_HEIGHT/2))
    
    global TILES
    global tiles
        
    current_map = map()
    current_map.load('1')
    TILES, tiles = current_map.build()
    
    ps = playState(player, camera(
                                  complex_camera,
                                  current_map.width(),
                                  current_map.height())
                   )
    ps.run()

"""
Handles input, blitting frames and fps
Future: will point to pause menu, home menu, etc
"""
class playState(object):
    
    """
    Define all of the object's variables in the __init__
    """
    def __init__(self, player, camera):
        self.UP = self.DOWN = self.LEFT = self.RIGHT = self.RUNNING = self.CLICK = False
        # 'bind' classes to the playstate class, for later use,
        # instead of leaving them floating in the 'global' realm
        self.player = player
        self.camera = camera

    """
    Draw the tiles that are in the array 'tiles'
    """
    def drawTiles(self, tiles):
        for t in tiles:
            screen.blit(t.image, self.camera.apply(t))
            
    """
    Routine operations happening each tick, from filling the screen to updating
    and drawing new player information
    """
    def runframe(self):
        screen.blit(background, (0, 0))
        
        self.camera.update(self.player)
        
        self.player.update(self.UP, self.DOWN, self.LEFT, self.RIGHT, self.RUNNING, TILES)
        mouse.update(pygame.mouse.get_pos(), self.CLICK)
        if mtext:
            mtext.update(pygame.mouse.get_pos())     
        
        self.drawTiles(tiles)
        
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