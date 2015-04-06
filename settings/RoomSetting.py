'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 23.04.2014
'''
from general.Color import Color
from entities.Plane import Plane
from entities.Sphere import Sphere
from general.HomVector import HomVector
from general.Camera import Camera
from general.Light import Light
from entities.materials.CheckerboardMaterial import CheckerboardMaterial

class RoomSetting(object):
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
        self.entities.append(Plane(HomVector(0, -1, 0, 1), HomVector(0, -1, 0, 0), color=(128, 128, 128), material=CheckerboardMaterial(), ambientCoefficient=0.8, diffuseCoefficient=0.2, specularCoefficient=0.2)) 
        self.entities.append(Plane(HomVector(0, 10, 0, 1), HomVector(0, -1, 0, 0), color=(128, 128, 128), material=CheckerboardMaterial(), ambientCoefficient=0.8, diffuseCoefficient=0.2, specularCoefficient=0.2)) 
        self.entities.append(Plane(HomVector(-5, 0, 0, 1), HomVector(1, 0, 0, 0), color=(128, 128, 128), material=CheckerboardMaterial(), ambientCoefficient=0.8, diffuseCoefficient=0.2, specularCoefficient=0.2))
        self.entities.append(Plane(HomVector(5, 0, 0, 1), HomVector(-1, 0, 0, 0), color=(128, 128, 128), material=CheckerboardMaterial(), ambientCoefficient=0.8, diffuseCoefficient=0.2, specularCoefficient=0.2))
        self.entities.append(Sphere(HomVector(0, 4.6, -10, 1), 14, color=(0, 0, 0), reflects=True, ambientCoefficient=0.0, diffuseCoefficient=0.4, specularCoefficient=0.6)) 

        self.lights = []
        self.lights.append(Light(HomVector(0, 3.15, 5, 1), color=(255, 255, 255))) # white light
        
        if not self.showMaterial:
            for entity in self.entities:
                entity.showMaterial = False
                
    def setSize(self, width, height):
        """ Sets the size of the image and (re)configures the camera. """
        self.WIDTH = width
        self.HEIGHT = height
        self.PIXELCOUNT = self.WIDTH * self.HEIGHT
        self.progressStep = self.PIXELCOUNT / 100
        self.camera = Camera(HomVector(0, 1.8, 10, 1), HomVector(0, 3, 0, 1), HomVector(0, 1, 0, 0), 45, self.WIDTH, self.HEIGHT)