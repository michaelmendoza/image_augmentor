
import matplotlib.pyplot as plt
import math

from loader import Loader
from pointcloud import PointCloud

def test():
    image = Loader.load('smile.jpg')
    Loader.show(image)

    pcloud = PointCloud(image)
    pcloud.transform(scale=1.0, rotation=math.pi/2, translation=[200,0])
    #img = pcloud.resample()
    img = pcloud.sample([200,200])
        
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    test()
