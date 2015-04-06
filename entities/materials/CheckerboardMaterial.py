'''
Created on 18.04.2014

@author: Tilman Ginzel (173388)
'''
from general.Color import Color
from general.HomVector import HomVector

class CheckerboardMaterial(object):
    """ This class describes a simple Checkerboard material for entities. """
    def __init__(self, baseColor=Color(255, 255, 255), otherColor=Color(0, 0, 0), checkSize=1):
        self.baseColor = baseColor
        self.otherColor = otherColor
        self.checkSize = checkSize
        
    def baseColorAt(self, v, entity):
        """ Return color at position vector """
        v = HomVector(v.x, v.y, v.z, 0)
        v = v.scale(1.0 / self.checkSize)
        if (int(abs(v.x) + 0.5) + int(abs(v.y) + 0.5) + int(abs(v.z) + 0.5)) % 2:
            return self.otherColor
        return self.baseColor