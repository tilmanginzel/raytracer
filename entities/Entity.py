'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 16.04.2014
'''
from general.Color import Color
from general.Ray import Ray

class Entity(object):
    """ This class describes methods for all entities, no matter which shape. """
    def __init__(self, color=(128, 128, 128), reflects=False, material=None, ambientCoefficient=0.35, diffuseCoefficient=0.45, specularCoefficient=0.25):
        self.color = Color(color[0], color[1], color[2])
    
        self.ambientCoefficient = ambientCoefficient # ambient coefficient
        self.diffuseCoefficient = diffuseCoefficient # diffuse coefficient
        self.specularCoefficient = specularCoefficient # specular coefficient
        self.reflects = reflects # boolean: whether the object reflects or not
        self.material = material # surface material
        self.showMaterial = True
        self.shadowCoefficient = 0.95
    
    def getAmbientColor(self, intersectionPoint):
        """ Returns the ambient color of the entity, depending on its ambient coefficient and material. """
        if self.material and self.showMaterial:
            return self.ambientCoefficient * self.material.baseColorAt(intersectionPoint, self)
        else:
            return self.ambientCoefficient * self.color
    
    def getDiffuseColor(self, light, l, n):
        """ Returns the diffuse color of the entity, depending on its diffuse coefficient and the light source. """
        return light.color * self.diffuseCoefficient * l.dot(n)
    
    def getSpecularColor(self, light, lr, d):
        """ Returns the specular color of the entity, depending on its specular coefficient and the light source. """
        return light.color * self.specularCoefficient * lr.dot(d)**20
    
    def colorAt(self, ray, hitdist, lights, entityList):
        """ Calculates the final color of the entity, depending on light sources and other intersecting entities. """
        intersectionPoint = ray.pointAtParameter(hitdist)
        
        ambientColor = self.getAmbientColor(intersectionPoint)
        diffuseColor = Color(0, 0, 0)
        specularColor = Color(0, 0, 0)
        for light in lights:
            n = self.normalAt(intersectionPoint)
            l = (light.position - intersectionPoint).normalized()
            lr = (l.scale(-1) - n.scale((2 * l.scale(-1).dot(n)))).normalized()
            
            shadow = False
            for entity in entityList:
                distToLight = (light.position - intersectionPoint).length()
                rayToLight = Ray(intersectionPoint+ray.direction.scale(-0.00001), l)
                hitdist = entity.intersectionParameter(rayToLight)
                if hitdist and hitdist > 0 and distToLight > hitdist:
                    shadow = True
                    break
            
            if shadow:
                ambientColor = ambientColor * self.shadowCoefficient
            else:
                diffuseColor += self.getDiffuseColor(light, l, n)
                specularColor += self.getSpecularColor(light, lr, ray.direction)
            
        return ambientColor + diffuseColor + specularColor

        
    