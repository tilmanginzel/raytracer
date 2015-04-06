'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 06.04.2014
'''
from entities.Entity import Entity

class Plane(Entity):
    """ This class describes a plane entity. """
    
    def __init__(self, point, normal, color=(128, 128, 128), reflects=False, material=None, ambientCoefficient=0.35, diffuseCoefficient=0.45, specularCoefficient=0.25):
        Entity.__init__(self, color, reflects, material, ambientCoefficient, diffuseCoefficient, specularCoefficient)
        self.point = point # point
        self.normal = normal.normalized() # vector
        
    def __repr__(self):
        """ Returns a representation of the entity. """
        return 'Plane(%s, %s)' %(repr(self.point), repr(self.normal))
    
    def intersectionParameter(self, ray):
        """ Calculates the intersection point between itself and a ray and returns the hitdistance. """
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)
        if b:
            return -a/b
        else:
            return None

    def normalAt(self, p):
        """ Returns the normal vector at a given point. """
        return self.normal