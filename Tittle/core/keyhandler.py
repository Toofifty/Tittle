from pygame.locals import *

"""
Decides what to do on key presses
"""
def get_action(playstate, event):
    action = None
    for e in event:
        if e.type == KEYDOWN and e.type == QUIT: raise SystemExit, "QUIT"
        if e.type == KEYDOWN and e.key == K_ESCAPE: raise SystemExit, "ESCAPE"
        if e.type == KEYDOWN and e.key == K_RETURN: action = 'newplayer'
        
        if e.type == KEYDOWN and (e.key == K_SPACE or e.key == K_w or e.key == K_UP): playstate.UP = True
        if e.type == KEYDOWN and (e.key == K_s or e.key == K_DOWN): playstate.DOWN = True
        if e.type == KEYDOWN and (e.key == K_a or e.key == K_LEFT): playstate.LEFT = True
        if e.type == KEYDOWN and (e.key == K_d or e.key == K_RIGHT): playstate.RIGHT = True
        if e.type == KEYDOWN and e.key == K_LSHIFT: playstate.RUNNING = True
        if e.type == KEYDOWN and e.key == K_F11: action = 'fullscreen'
        
        
        if e.type == MOUSEBUTTONDOWN and e.button == 1: playstate.CLICK = True
        
        if e.type == KEYUP and (e.key == K_SPACE or e.key == K_w or e.key == K_UP): playstate.UP = False
        if e.type == KEYUP and (e.key == K_s or e.key == K_DOWN): playstate.DOWN = False
        if e.type == KEYUP and (e.key == K_a or e.key == K_LEFT): playstate.LEFT = False
        if e.type == KEYUP and (e.key == K_d or e.key == K_RIGHT): playstate.RIGHT = False
        if e.type == KEYUP and e.key == K_LSHIFT: playstate.RUNNING = False
        if e.type == MOUSEBUTTONUP and e.button == 1: playstate.CLICK = False
        
        if not action:
            action = False
        
    return action