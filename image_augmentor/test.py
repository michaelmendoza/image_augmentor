
from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt
import math

from .augmentor import Augmentor
from .loader import Loader
from .transform import Transform
from .sample import Sample

def image_augment_test(foldername):
    aug = Augmentor()
    imgs = aug.run(foldername)

    plt.ion()
    for img in imgs:
        plt.imshow(img, cmap='gray')
        plt.pause(0.05)

def image_array_augment_test(foldername):

    image_array = Loader.loadFolder2(foldername)

    aug = Augmentor()
    imgs = aug.run(image_array)

    plt.ion()
    for img in imgs:
        plt.imshow(img, cmap='gray')
        plt.pause(0.05)

def transform_test(filename):
    image = Loader.load(filename)
    Loader.show(image) 
    transform = Transform(scale = 0.8, rotation=math.pi / 2, translation=[0.1, 0.2 ])
    img = Sample.sample(image, transform)    
    print(img.shape)
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    #image_augment_test()
    image_array_augment_test()
    #transform_test()
