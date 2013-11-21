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
        textimage = pygame.Surface((len(schars) * self.charw, self.charh)).convert_alpha()
        textimage.fill((0, 255, 255))
        for i, char in enumerate(schars):
            textimage.blit(self.chars[char], (i * self.charw, 0))
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



"""
Font class that maps a list of supported chars to their corresponding images.
This is then used to get an image for a given piece of text.
""""""
class Font:
    
    def __init__(self, supportedChars, charImages):
        self.chars = {}
        for i, char in enumerate(supportedChars):
            self.chars[char] = charImages[i]
        self.charWidth = charImages[0].get_width()
        self.charHeight = charImages[0].get_height()
            
    def getTextImage(self, text):
        # filter out any unsupported chars
        supportedText = [c for c in text if c in self.chars]
        textImage = view.createTransparentRect((len(supportedText) * self.charWidth, self.charHeight))
        for i, char in enumerate(supportedText):
            textImage.blit(self.chars[char], (i * self.charWidth, 0))
        return textImage
            
class GameFont(Font):

    fontImage = None
    
    def __init__(self):
        if GameFont.fontImage is None:    
            imagePath = os.path.join("assets" ,FONT_FOLDER, "font.png")
            GameFont.fontImage = view.loadScaledImage(imagePath, None)        
        charImages = view.processFontImage(GameFont.fontImage, 8, 3)
        Font.__init__(self, CHARS, charImages)
        
class NumbersFont(Font):

    fontImage = None
    
    def __init__(self):
        if NumbersFont.fontImage is None:    
            imagePath = os.path.join(FONT_FOLDER, "numbers.png")
            NumbersFont.fontImage = view.loadScaledImage(imagePath, None)        
        charImages = view.processFontImage(NumbersFont.fontImage, 8 * SCALAR)
        Font.__init__(self, NUMBERS, charImages)"""