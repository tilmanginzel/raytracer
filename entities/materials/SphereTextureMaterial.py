'''
Created on 20.04.2014

@author: Tilman Ginzel (173388)
'''
from general.Color import Color
from math import  pi,  asin
from PIL import Image

class SphereTextureMaterial(object):
    """ This material maps an image on a sphere entity. """
    def __init__(self, filename=None):
        if filename:
            self.image = Image.open(filename)
            size = self.image.size
            self.width = size[0]
            self.height = size[1]
            self.rgbImage = self.image.convert('RGB')
        else:
            self.image = None
    
    def baseColorAt(self, p, entity):
        """ Return color at point from image file """
        if not self.image:
            return Color(0, 0, 0)
        
        normal = entity.normalAt(p)
        nx = normal.x
        ny = normal.y
        
        tu = asin(nx)/pi + 0.5
        tv = asin(ny)/pi + 0.5
        
        x = int(tu*self.width) / 2
        y = self.height- int(tv*self.height)
        r, g, b = self.rgbImage.getpixel((x, y))
        
        return Color(r, g, b)
        