'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 06.04.2014
'''
from math import sqrt
from entities.Entity import Entity

class Sphere(Entity):
    """ This class describes a sphere entity. """
    
    def __init__(self, center, radius, color=None, reflects=False, material=None, ambientCoefficient=0.35, diffuseCoefficient=0.45, specularCoefficient=0.25):
        Entity.__init__(self, color, reflects, material, ambientCoefficient, diffuseCoefficient, specularCoefficient)
        self.center = center # point
        self.radius = radius #scalar
        
    def __repr__(self):
        """ Returns a representation of the entity. """
        return 'Sphere(%s, %f)' %(repr(self.center), self.radius)
    
    def intersectionParameter(self, ray):
        """ Calculates the intersection point between itself and a ray and returns the hitdistance. """
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v*v - co.dot(co) + self.radius*self.radius
        if discriminant < 0:
            return None
        else:
            return v - sqrt(discriminant)

    def normalAt(self, p):
        """ Returns the normal vector at a given point. """
        return (p - self.center).normalized()