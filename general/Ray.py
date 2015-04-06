'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 06.04.2014
'''

class Ray(object):
    """ This class represents a ray with an origin and a direction. """
    
    def __init__(self, origin, direction):
        self.origin = origin # point
        self.direction = direction.normalized() # vector
        
    def pointAtParameter(self, t):
        """ Returns a point on this ray at a given parameter t. """
        return self.origin + self.direction.scale(t)
    
    def __repr__(self):
        """ Returns a representation of itself. """
        return 'Ray(%s, %s)' %(repr(self.origin), repr(self.direction))