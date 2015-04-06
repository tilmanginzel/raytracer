'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 17.04.2014
'''
from general.Color import Color

class Light(object):
    """ This class describes the position and color of a light source. """
    
    def __init__(self, position, color=(255, 255, 255)):
        self.position = position
        self.color = Color(color[0], color[1], color[2])