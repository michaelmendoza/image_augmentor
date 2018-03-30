
import math
import numpy as np
from tqdm import trange, tqdm

from options import AugmentOptions
from loader import Loader
from transform import Transform
from sample import Sample

class Augmentor:
    def __init__(self):
        self.options = AugmentOptions() 

    def run(self, filepath, count):
        
        image = Loader.load('smile.jpg')        
        imgs = []

        for _ in tqdm(range(count)):
            #print(_)
            options = self.options 
            scale = np.random.rand() * (options.scale[1] - options.scale[0]) + options.scale[0]
            rotate = np.random.rand() * (options.rotate[1] - options.rotate[0]) + options.rotate[0]
            tx = np.random.rand() * (options.tx[1] - options.tx[0]) + options.tx[0]
            ty = np.random.rand() * (options.ty[1] - options.ty[0]) + options.ty[0]
            transform = Transform(scale = scale, rotation = rotate, translation = [tx, ty])
            imgs.append(Sample.sample(image, transform) )

        return imgs
