#!/usr/bin/env python


import base, pygame
import xml.etree.ElementTree as et

from sprites import gameSprite

"""
Creates an 'item' object (gamesprite) ready to be loaded into game
"""
class item(gameSprite):
    """
    Grabs the sprite image from 'items_sheet.png' > item_rect, converts, and sets rect
    based on image. 
    """    
    def __init__(self, item_rect, item_name):
        self.image = spriteSheet(SPRITES_FOLDER + 'items_sheet.png').image_at(item_rect).convert_alpha()
        self.rect = Rect((0, 0),(item_rect.height, item_rect.width))
        
        info = readTxt(ITEMS_FOLDER + '/' + item_name + '.txt')
        
    """
    Simple return methods
    If the method doesn't have a try statement, all items should have said
    attribute
    """
    def getType(self):
        return self.type
    
    def getClass(self):
        try: return self.weapon_class
        except: print "Error: (items has no weapon_class attribute?)", sys.exc_info()[0]
    
    def getTier(self):
        try: return self.tier
        except: print "Error (item has no tier attribute?): ", sys.exc_info()[0]
    
    def getProtection(self):
        try: return self.protection
        except: print "Error (item has no protection attribute?): ", sys.exc_info()[0]
    
    def getWeight(self):
        return self.weight
    
    def getDurability(self):
        return self.durability
    
    def getDamage(self):
        try: return self.damage
        except: print "Error (item has no damage attribute?): ", sys.exc_info()[0]
        
    def getRange(self):
        try: return self.range
        except: print "Error (item has no range attribute?): ", sys.exc_info()[0]
        
    def getRate(self):
        try: return self.rate
        except: print "Error (item has no rate attribute?): ", sys.exc_info()[0]
        
        
"""
Loads all item data from the items.xml file
"""
class itemData(object):
    """
    
    """
    def __init__(self):
        tree = et.parse('../assets/items.xml')
        self.data = tree.getroot()
        """
        for child in self.data:
            print '\n'
            print child.get('name')
            for grandchild in child:
                print '   ', grandchild.tag,': ', grandchild.text"""
                
    """
    Returns all data for item_name provided
    (no format or order yet, soo... don't use)
    """
    def getData(self, item_name):
        attribs = []
        for item in self.data:
            if item.get('name') == item_name:
                print 'found item: ',item_name
                for attrib in item:
                    attribs.append(attrib.text)
                    
        return attribs
