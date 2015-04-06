'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 16.04.2014
'''
class Color(object):
    """ This class describes a color object. """
    
    def __init__(self, r, g, b):
        """ The constructor checks whether the given components are between 0 <= r, g, b <= 255. """
        self.r = max(min(r, 255), 0)
        self.g = max(min(g, 255), 0)
        self.b = max(min(b, 255), 0)
        
    def __add__(self, color):
        """ Adds two colors via additive mixing. """
        return Color(min(self.r + color.r, 255), min(self.g + color.g, 255), min(self.b + color.b, 255))
    
    def __mul__(self, t):
        """ Multiplies each color component with a given factor. """
        r = max(min(self.r*t, 255), 0)
        g = max(min(self.g*t, 255), 0)
        b = max(min(self.b*t, 255), 0)
        return Color(r, g, b)
    
    def __rmul__(self, t):
        return self.__mul__(t)

    def mix(self, c):
        """ Mixes two colors via subtractive mixing. """
        return Color((self.r+c.r)/2, (self.g+c.g)/2, (self.b+c.b)/2)
    
    def __repr__(self):
        """ Returns a representation of itself. """
        return "Color(%s, %s, %s)" %(self.r, self.g, self.b)