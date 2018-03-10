
import numpy as np

from transform import AffineTransform
from resample import Resample

class PointCloud:

    def __init__(self, image):
        ''' Generate a point cloud from an image '''
        self.cloud = [];
        for r in range(image.shape[0]):
            for c in range(image.shape[1]):
                self.cloud.append([r, c, image[r,c]])

    def transform(self, scale, rotation, translation):
        t = AffineTransform(scale=scale, rotation=rotation, translation=translation)
        self.cloud = t.transform(self.cloud)

    def inverseTransform(self):
        pass

    def resample(self):
        img = Resample.resample(np.array(self.cloud))
        return img