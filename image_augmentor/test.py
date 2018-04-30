
from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt
import math

from .augmentor import Augmentor
from .loader import Loader
from .transform import Transform
from .sample import Sample

def transform_test(filename):
    image = Loader.load(filename)
    Loader.show(image) 
    transform = Transform(scale = 0.8, rotation=math.pi / 2, translation=[0.1, 0.2 ])
    img = Sample.sample(image, transform)    
    print(img.shape)
    plt.imshow(img, cmap='gray')
    plt.show()

def image_augment_test(foldername):
    aug = Augmentor()
    imgs = aug.run(foldername, 10)

    plt.ion()
    for img in imgs:
        plt.imshow(img, cmap='gray')
        plt.pause(0.05)

if __name__ == '__main__':
    image_augment_test()
    #transform_test()
