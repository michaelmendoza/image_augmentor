
import math

class AugmentOptions:
    def __init__(self):
        ''' Interations of image augmentation '''
        self.interations = 10

        ''' Probabilty of transformation'''
        self.pScale = 0.5
        self.pRotate = 0.5
        self.pTranslate = 0.5

        ''' Min/Max values for transformation '''
        self.scale = (0.8, 1.2)
        self.rotate = (0.0, math.pi)
        self.tx = (-0.2, 0.2)
        self.ty = (-0.2, 0.2)
