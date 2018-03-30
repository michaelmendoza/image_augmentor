
import math
import numpy as np

from loader import Loader
from transform import Transform
from sample import Sample

class AugmentOptions:
    def __init__(self):
        ''' Probabilty of transformation'''
        self.pScale = 0.5
        self.pRotate = 0.5
        self.pTranslate = 0.5

        ''' Min/Max values for transformation '''
        self.scale = (0.8, 1.2)
        self.rotate = (0.0, math.pi)
        self.tx = (-0.2, 0.2)
        self.ty = (-0.2, 0.2)

options = AugmentOptions()

class Augmentor:
    def __init__(self):
        self.options = options  

    def run(self, filepath, count):
        
        image = Loader.load('smile.jpg')        
        imgs = []
        for _ in range(count):
            print(_)
            scale = np.random.rand() * (options.scale[1] - options.scale[0]) + options.scale[0]
            rotate = np.random.rand() * (options.rotate[1] - options.rotate[0]) + options.rotate[0]
            tx = np.random.rand() * (options.tx[1] - options.tx[0]) + options.tx[0]
            ty = np.random.rand() * (options.ty[1] - options.ty[0]) + options.ty[0]
            transform = Transform(scale = scale, rotation = rotate, translation = [tx, ty])
            imgs.append(Sample.sample(image, transform) )

        return imgs
