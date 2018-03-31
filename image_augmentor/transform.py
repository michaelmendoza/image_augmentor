
from __future__ import absolute_import, division, print_function

import numpy as np

from math import cos, sin
from .point import Point

class Transform:
    ''' Simple implementation for a affine transformation with scaling, rotation and translation '''

    def __init__(self, scale=1.0, rotation=0.0, translation=[0,0]):
        ''' Initalize affine transformation matrix (H) '''
        s = scale
        r = rotation
        tx = translation[0] + translation[0] # Doubled tx due to normalized space being in (-1, 1)
        ty = translation[1] + translation[1] # Doubled ty due to normalized space being in (-1, 1)
        H = [[s*cos(r), -s*sin(r), tx],
             [s*sin(r), s*cos(r),  ty],
             [0.0,        0.0,    1.0]]
        self.H = np.array(H)
        self.Hinv = np.linalg.inv(self.H)

    def transform(self, points):
        ''' Transform points with affine transformation '''
        new_points = []
        for point in points:
            u = np.array([point[0], point[1], 1])       # Set to homogeneous coordinates
            x = np.dot(self.H, u)                       # Apply transformation
            new_points.append(Point(x=x[0], y=x[1]))
        return new_points

    def inverse_transform(self, points):
        ''' Transform points with inverse affine transformation '''
        new_points = []
        for point in points:
            u = np.array([point.x, point.y, 1])          # Set to homogeneous coordinates
            x = np.dot(self.Hinv, u)                     # Apply transformation
            new_points.append(Point(x=x[0], y=x[1]))
        return new_points 
