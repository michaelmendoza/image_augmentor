
from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt
import math

from image_augmentor.augmentor import Augmentor
from image_augmentor.loader import Loader
from image_augmentor.transform import Transform
from image_augmentor.sample import Sample

def transform_test():
    image = Loader.load('images\smile.jpg')
    Loader.show(image) 
    transform = Transform(scale = 0.8, rotation=math.pi / 2, translation=[0.1, 0.2 ])
    img = Sample.sample(image, transform)    
    print(img.shape)
    plt.imshow(img, cmap='gray')
    plt.show()

def image_augment_test():
    aug = Augmentor()
    imgs = aug.run('images', 10)

    plt.ion()
    for img in imgs:
        plt.imshow(img, cmap='gray')
        plt.pause(0.05)

if __name__ == '__main__':
    image_augment_test()
    #transform_test()
