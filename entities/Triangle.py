'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 09.04.2014
'''
from entities.Entity import Entity

class Triangle(Entity):
    """ This class describes a triangle entity. """
    
    def __init__(self, a, b, c, color=(128, 128, 128), reflects=False, material=None, ambientCoefficient=0.35, diffuseCoefficient=0.45, specularCoefficient=0.25):
        Entity.__init__(self, color, reflects, material, ambientCoefficient, diffuseCoefficient, specularCoefficient)
        self.a = a # point
        self.b = b # point
        self.c = c # point
        self.u = self.b - self.a # direction vector
        self.v = self.c - self.a # direction vector
        
    def __repr__(self):
        """ Returns a representation of the entity. """
        return 'Triangle(%s, %s, %s)' %(repr(self.a), repr(self.b), repr(self.c))
    
    def intersectionParameter(self, ray):
        """ Calculates the intersection point between itself and a ray and returns the hitdistance. """
        w = ray.origin - self.a
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu
        if 0 <= r and r <= 1 and 0 <= s and s <= 1 and r+s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        """ Returns the normal vector at a given point. """
        return self.u.cross(self.v).normalized()