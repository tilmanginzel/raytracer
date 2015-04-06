'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 18.04.2014
'''
class HitPointData(object):
    """ This class is used to hold hit point data including the entity, hitdist and the ray. """
    def __init__(self, entity, hitdist, ray):
        self.entity = entity
        self.hitdist = hitdist
        self.ray = ray
        
    def __repr__(self):
        """ Returns a representation of the entity. """
        return 'HitPointData(%s, %s, %s)' %(repr(self.entity), self.hitdist, repr(self.ray))
        