'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 08.04.2014
'''
from general.Ray import Ray
from math import tan, pi

class Camera(object):
    """ This class describes the camera. """
    def __init__(self, e, c, up, fieldOfView, wRes, hRes):
        self.e = e # position
        self.c = c # center
        self.up = up # up
        self.wRes = float(wRes) # image width
        self.hRes = float(hRes) # image height
        
        self.alpha = (fieldOfView/180. * pi) / 2.
        
        self.height = 2 * tan(self.alpha)
        self.width = (self.wRes/self.hRes) * self.height

        self.f = (self.c - self.e).normalized() # vector to center ('z-axis' vector) 
        self.s = (self.f.cross(self.up)).normalized() # 'x-axis' vector
        self.u = self.s.cross(self.f) # 'y-axis' vector
        
    def calcRay(self, x, y):
        """ Calculates a ray depending on its camera parameters and x and y pixels and . """
        pixelWidth = self.width / (self.wRes - 1)
        pixelHeight = self.height/ (self.hRes - 1)
        xcomp = self.s.scale(x*pixelWidth - self.width/2.)
        ycomp = self.u.scale(y*pixelHeight - self.height/2.)

        return Ray(self.e, self.f + xcomp + ycomp)
    
    def calcRays(self, x, y):
        return self.ssaa4(x, y)
    
    def ssaa4(self, x, y):
        """ Returns 4 different rays with a small offset to the original position. This enables 4x supersample antialiasing. """
        rays = []
        rays.append(self.calcRay(x+0.25, y))
        rays.append(self.calcRay(x-0.25, y))
        rays.append(self.calcRay(x, y+0.25))
        rays.append(self.calcRay(x, y-0.25))
        return rays
        
    def ssaa8(self, x, y):
        """ Returns 8 different rays with a small offset to the original position. This enables 8x supersample antialiasing. """
        rays = []
        rays.append(self.calcRay(x+0.5, y+0.25))
        rays.append(self.calcRay(x+0.25, y+0.5))
        rays.append(self.calcRay(x-0.5, y+0.25))
        rays.append(self.calcRay(x-0.25, y+0.5))
        rays.append(self.calcRay(x-0.5, y-0.25))
        rays.append(self.calcRay(x-0.25, y-0.5))
        rays.append(self.calcRay(x+0.5, y-0.25))
        rays.append(self.calcRay(x+0.25, y-0.5))
        return rays
        