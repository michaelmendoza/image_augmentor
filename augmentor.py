
import os
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
        
        print('Loading image files ... ')
        files = os.listdir(filepath)
        data = []
        for file in tqdm(files):
            data.append(Loader.load(filepath + "\\" + file))

        print('Augmenting image set ... ')
        aug_images = []
        for _ in tqdm(range(count)):
            for image in data:
                options = self.options 
                scale = np.random.rand() * (options.scale[1] - options.scale[0]) + options.scale[0]
                rotate = np.random.rand() * (options.rotate[1] - options.rotate[0]) + options.rotate[0]
                tx = np.random.rand() * (options.tx[1] - options.tx[0]) + options.tx[0]
                ty = np.random.rand() * (options.ty[1] - options.ty[0]) + options.ty[0]
                transform = Transform(scale = scale, rotation = rotate, translation = [tx, ty])
                aug_images.append(Sample.sample(image, transform) )

        return aug_images
