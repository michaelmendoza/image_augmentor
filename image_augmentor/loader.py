
from __future__ import absolute_import, division, print_function

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
from tqdm import trange, tqdm

class Loader:
    def __init__(self):
        pass

    def rgb2grey(self, image):
        """ Generate a grey image in a 2-D numpy array (row, col) Range: 0 - 255 """
        r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
        return 0.2989 * r + 0.5870 * g + 0.1140 * b

    def load(self, filename):
        image = mpimg.imread(filename)
        image = self.rgb2grey(image)
        return image;

    def loadFolder(self, foldername):
        files = os.listdir(foldername)
        data = []
        for file in tqdm(files):
            _file = os.path.join(foldername, file)
            data.append(Loader.load(_file))
        return data

    def show(self, image):
        plt.imshow(image, cmap='gray')
        plt.show()
    
Loader = Loader()