
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

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

    def show(self, image):
        plt.imshow(image, cmap='gray')
        plt.show()
    
Loader = Loader()