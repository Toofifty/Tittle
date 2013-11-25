#! /usr/bin/env python

import os, pygame

CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"',
         '#', '$', '%', '&','\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
         '>', '=', '?', '@', '[', ']','\\', '^', '_', '{', '|', '}', ' ']

class font:
    
    def __init__(self, charimages):
        self.chars = {}
        for i, char in enumerate(CHARS):
            self.chars[char] = charimages[i]
        self.charw = charimages[0].get_width()
        self.charh = charimages[0].get_height()
        print self.charw, self.charh
        
    def text(self, text):
        schars = [c for c in text if c in self.chars]
        textimage = pygame.Surface(((len(schars)+2) * self.charw, 2*self.charh)).convert()
        textimage.fill((0, 0, 255))
        textimage.set_colorkey((0, 0, 255), pygame.RLEACCEL)
        for i, char in enumerate(schars):
            textimage.blit(self.chars[char], ((i+1) * self.charw, self.charh/2))
        return textimage
            
class gamefont(font):
    fontimage = None
    
    def __init__(self):
        if self.fontimage is None:
            self.fontimage = pygame.image.load('assets/sprites/3dfont.png').convert_alpha()
        charimages = []
        charheight = self.fontimage.get_height() // 6
        for i in range(6):
            x, y = 0, i * charheight
            while x < self.fontimage.get_width():
                charimage = self.fontimage.subsurface((x, y), (8, charheight))
                charimages.append(charimage)
                x += 8
        font.__init__(self, charimages)
        print charimages
