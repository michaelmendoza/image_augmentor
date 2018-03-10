
import numpy as np
from math import cos, sin

class AffineTransform():

    def __init__(self, scale=1.0, rotation=0.0, translation=[0,0]):
        ''' Initalize affine transformation matrix (H) '''
        s = scale
        r = rotation
        tx = translation[0]
        ty = translation[1]
        H = [[s*cos(r), -s*sin(r), tx],
             [s*sin(r), s*cos(r),  ty],
             [0.0,        0.0,    1.0]]
        self.H = np.array(H)

    def set_matrix(self, H):
        self.H = H

    def transform(self, points):
        ''' Transform points with affine transformation '''
        new_points = []
        for point in points:
            u = np.array([point[0], point[1], 1]) # Set to homogeneous coordinates
            x = np.dot(self.H, u) # Apply transformation
            x[2] = point[2] # Format data to point [x, y, value]
            new_points.append(x.tolist())
        return new_points

    def inverse_transform(self, points):
        ''' Transform points with inverse affine transformation '''
        new_points = []
        Hinv = np.linalg.inv(self.H)
        for point in points:
            u = np.array([point[0], point[1], 1]) # Set to homogeneous coordinates
            x = np.dot(Hinv, u) # Apply transformation
            x[2] = point[2] # Format data to point [x, y, value]
            new_points.append(x.tolist())
        return new_points 

    