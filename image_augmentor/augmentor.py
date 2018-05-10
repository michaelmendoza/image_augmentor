
from __future__ import absolute_import, division, print_function

import os
import math
import numpy as np
from tqdm import trange, tqdm

from .options import AugmentOptions
from .loader import Loader
from .transform import Transform
from .sample import Sample

def isArray(arr):
    return hasattr(arr, 'shape')

class Augmentor:
    def __init__(self):
        pass

    def run(self, data, options = AugmentOptions()):
        
        if not isArray(data):
            print('Loading image files ... ')
            data = Loader.loadFolder2(data)

        print('Shape of input image data:', data.shape)
        print('Augmenting image set ... ')
        
        aug_images = None
        for _ in tqdm(range(options.interations)):
            for image in data:
                scale = np.random.rand() * (options.scale[1] - options.scale[0]) + options.scale[0]
                rotate = np.random.rand() * (options.rotate[1] - options.rotate[0]) + options.rotate[0]
                tx = np.random.rand() * (options.tx[1] - options.tx[0]) + options.tx[0]
                ty = np.random.rand() * (options.ty[1] - options.ty[0]) + options.ty[0]
                transform = Transform(scale = scale, rotation = rotate, translation = [tx, ty])
                image = Sample.sample(image, transform)
                
                if not isArray(aug_images):
                    aug_images = np.expand_dims(image, axis=0)
                else:
                    aug_images = np.concatenate( (aug_images, image[None,:]), axis=0)

        print('Shape of augmented image data:', aug_images.shape)
        return aug_images
