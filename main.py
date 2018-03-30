
import matplotlib.pyplot as plt
import math

from loader import Loader
from transform import Transform
from sample import Sample

def test():
    image = Loader.load('smile.jpg')
    Loader.show(image)
    transform = Transform(rotation=math.pi / 2)
    img = Sample.sample(image, transform)    
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    test()
