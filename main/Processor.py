'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 18.04.2014
'''
from general.Color import Color
from general.Ray import Ray
from general.HitPointData import HitPointData

class Processor(object):
    """ This class is used to initiate the raytracing process. """
    
    def __init__(self, settings, display=True, ssaa=False):
        self.settings = settings
        self.display = display # display is relevant if the script is executed via a ssh connection on a server, otherwise you cannot see the progress
        self.ssaa = ssaa # flag for supersample antialiasing
    
    def startProcessing(self):
        """ This method goes through every pixel and yields the color at this pixel. """
        
        processedPixels = 0
        for x in range(self.settings.WIDTH):
            for y in range(self.settings.HEIGHT):
                ray = self.settings.camera.calcRay(x, y)
                color = self.traceRay(0, ray)
                
                if self.ssaa: # if supersample antialiasing is activated, calculate more rays and mix the colors
                    for ray in self.settings.camera.ssaa4(x, y):
                        color = color.mix(self.traceRay(0, ray))
                        
                yield (x, (self.settings.HEIGHT-y)-1), (int(color.r), int(color.g), int(color.b))
                
                processedPixels += 1
                if processedPixels % self.settings.progressStep == 0:
                    print str((processedPixels / float(self.settings.PIXELCOUNT))*100)+'% processed...'+ ('\r' if self.display else '\n'),
            processedPixels += 1
        print 
    
    def traceRay(self, level, ray):
        """ Traces a ray, if it hits an reflecting entity, recursively to a set maximum depth. """
        
        hitPointData = self.intersect(level, ray)
        if hitPointData:
            return self.shade(level, hitPointData)
        
        return self.settings.BACKGROUND_COLOR
        
    def shade(self, level, hitPointData):
        """ Returns the color of an entity at the given hitpoint data. """
        
        directColor = hitPointData.entity.colorAt(hitPointData.ray, hitPointData.hitdist, self.settings.lights, self.settings.entities)
        
        reflectedRay = self.computeReflectedRay(hitPointData)
        reflectedColor = Color(0, 0, 0)
    
        if(hitPointData.entity.reflects):
            reflectedColor = self.traceRay(level + 1, reflectedRay) * 0.2
        
        return directColor + reflectedColor
        
    def computeReflectedRay(self, hitPointData):
        """ Computes an reflected ray depending on the hitpoint data. """    
        origin = hitPointData.ray.pointAtParameter(hitPointData.hitdist)
        origin += hitPointData.entity.normalAt(origin).scale(0.00001)
        d = hitPointData.ray.direction
        n = hitPointData.entity.normalAt(origin)
        newDirection = d - n.scale((n.dot(d)*2))
        return Ray(origin, newDirection.normalized())
        
    def intersect(self, level, ray):
        """ Checks if a ray intersects with an entity and returns relevant hitpoint data. """
        
        if level == int(self.settings.recursiveDepth):
            return None
        
        maxdist = float('inf')
        hitPointData = None
        for entity in self.settings.entities:
            hitdist = entity.intersectionParameter(ray)
            if hitdist and hitdist >= 0:
                if hitdist < maxdist:
                    maxdist = hitdist
                    hitPointData = HitPointData(entity, hitdist, ray) 
        
        return hitPointData
        
        
    