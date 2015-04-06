'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 20.04.2014
'''
from general.Color import Color
from general.HomVector import HomVector
from general.Camera import Camera
from general.Light import Light
from entities.Sphere import Sphere
from entities.materials.SphereTextureMaterial import SphereTextureMaterial

class SpaceSetting(object):
    """
    This class is used to initialize import settings such as image size, background color, recursive depth etc.
    Furthermore you can configure the camera and add several entities and light sources to the scene.
    """
    
    def __init__(self, width=400, height=400, recursiveDepth=3, showMaterial=False):
        self.setSize(width, height)
        self.showMaterial = showMaterial
        self.BACKGROUND_COLOR = Color(0, 0, 0)
        self.recursiveDepth = recursiveDepth
        
        self.entities = []
        self.entities.append(Sphere(HomVector(-1.5, -0.5, 0, 1), 2, color=(0, 255, 0), material=SphereTextureMaterial(filename='earth_texture_4096.jpg'), reflects=False, ambientCoefficient=0.2, diffuseCoefficient=0.7, specularCoefficient=0.1)) # earth
        self.entities.append(Sphere(HomVector(2, 2,-2.8, 1), 2*0.2727986, color=(0, 255, 0), material=SphereTextureMaterial(filename='moonmap.jpg'), reflects=False, ambientCoefficient=0.2, diffuseCoefficient=0.7, specularCoefficient=0.1)) # moon
        
        self.lights = []
        self.lights.append(Light(HomVector(30, 30, 10, 1), color=(255, 255, 255))) # white light
        
        if not self.showMaterial:
            for entity in self.entities:
                entity.showMaterial = False
                
    def setSize(self, width, height):
        """ Sets the size of the image and (re)configures the camera. """
        self.WIDTH = width
        self.HEIGHT = height
        self.PIXELCOUNT = self.WIDTH * self.HEIGHT
        self.progressStep = self.PIXELCOUNT / 100
        self.camera = Camera(HomVector(0, 0, 6, 1), HomVector(0, 0, 0, 1), HomVector(0, 1, 0, 0), 45, self.WIDTH, self.HEIGHT)