
import matplotlib.pyplot as plt
import math

from loader import Loader
from pointcloud import PointCloud

def test():
    image = Loader.load('smile.jpg')
    Loader.show(image)

    pcloud = PointCloud(image)
    pcloud.transform(scale=1.0, rotation=math.pi/4, translation=[200,200])
    img = pcloud.resample()

    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    test()
