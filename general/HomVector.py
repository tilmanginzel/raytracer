'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 11.04.2014
'''
from math import sqrt
from general.HomVectorException import HomVectorException

class HomVector(object):
    """ 
    This class describes vectors and points with homogeneous coordinates. 
    If the fourth component equals 0, it represents a vector, otherwise a point. 
    """
    
    def __init__(self, x, y, z, h):
        self.x = float(x)   # x-coordinate
        self.y = float(y)   # y-coordinate
        self.z = float(z)   # z-coordinate
        self.h = float(h)   # homogeneous coordinate, 0: vector, 1: point
        
    def normalized(self):
        """ Sets the length of a vector to 1. """
        if self.h == 0:
            length = self.length()
            self.x = self.x / length
            self.y = self.y / length
            self.z = self.z / length
            return self
        else:
            raise HomVectorException('Points cannot be normalized')
        
    def length(self):
        """ Returns the length of a vector. """
        if self.h == 0:
            return sqrt(self.x**2 + self.y**2 + self.z**2)
        else:
            raise HomVectorException('Points have no length')
        
    def scale(self, t):
        """ Scales a vector with a given factor t. """
        if not self.isNumber(t):
            raise HomVectorException(str(t)+ ' is not a number')
        elif self.h == 0:
            return HomVector(self.x*t, self.y*t, self.z*t, self.h)
        else:
            raise HomVectorException('Points cannot be scaled')
        
    def dot(self, v):
        """ Calculates the dot product from two vectors and returns it. """
        if type(v) is not type(self):
            raise HomVectorException('the given parameter is no HomVector')
        elif self.h == 0 and v.h == 0:
            return self.x * v.x + self.y * v.y + self.z * v.z
        else:
            raise HomVectorException('points are not allowed here')
        
    def cross(self, v):
        """ Calculates the cross product from two vectors and returns it. """
        if type(v) is not type(self):
            raise Exception('the given parameter is no HomVector')
        elif self.h == 0 and v.h == 0:
            return HomVector(self.y*v.z - self.z*v.y,
                             -1*(self.x*v.z - self.z*v.x),
                             self.x*v.y - self.y*v.x,
                             self.h)
        else:
            raise HomVectorException('points are not allowed here')
    
    def __add__(self, v):
        """ Adds up two vectors by adding their components. """
        if type(v) is not type(self):
            raise Exception('the given parameter is no HomVector')
        elif v.h == 1 and self.h == 1:
            raise HomVectorException('you cannot add two points')
        else:
            return HomVector(self.x+v.x, self.y+v.y, self.z+v.z, self.h + v.h).adjust()
        
    def __radd__(self, v):
        return self.__add__(v)
        
    def __div__(self, t):
        """ Divides each vector component with a given divisor t. """
        if not self.isNumber(t):
            raise HomVectorException(str(t)+ ' is not a number')
        elif self.h == 0:
            return HomVector(self.x/t, self.y/t, self.z/t, self.h)
        else:
            raise HomVectorException('Points cannot be divided')
    
    def __sub__(self, v):
        """ Subtracts two HomVectors by subtracting each component. """
        if type(v) is not type(self):
            raise HomVectorException('the given parameter is no HomVector')
        else:
            return HomVector(self.x-v.x, self.y-v.y, self.z-v.z, self.h-v.h).adjust()
    
    def __rsub__(self, v):
        return self.__sub__(v)
    
    def __mul__(self, t):
        return self.scale(t)
    
    def __rmul__(self, t):
        return self.scale(t)
        
    def __repr__(self):
        return 'HomVector(%s, %s, %s, %s)' %(self.x, self.y, self.z, self.h)
    
    def adjust(self):
        """ Adjusts a HomVector so its fourth component will always equal 1 or 0. """
        if self.h != 0:
            self.x /= self.h
            self.y /= self.h
            self.z /= self.h
            self.h /= self.h
        return self
    
    def isNumber(self, t):
        """ Checks whether a given parameter t is a number. Complex numbers with imaginary units will be ignored. """
        try:
            float(t)
            return True
        except:
            return False
