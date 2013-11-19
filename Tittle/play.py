#! /usr/bin/env python

import pygame
import core.states

from pygame.locals import *


"""
Initialise pygame
"""
pygame.init()
pygame.mixer.init()

"""
Start the game, initialise the play state and
begin the handleInput game loop
"""
def main():
    # run game startup
    core.states.startGame()
    
    # main loop for the game   
    core.states.playState().handleInput()

"""
Calls the main() function when code is executed
"""
if __name__ == '__main__': main()
