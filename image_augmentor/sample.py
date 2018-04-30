
from __future__ import absolute_import, division, print_function
from math import cos, sin

import numpy as np
import time
import math

from .point import Point

class Sample:

    def sample(self, image, transform = None, Nx = 200, Ny= 200):
        
        ''' Sample grid in transformed space '''
        sample_points = [Point(x = c, y = r, bounding_box = (Ny, Nx)) for r in range(Nx) for c in range(Ny)]
        ''' Inverse transform into image space and get sample points '''
        original_points = transform.inverse_transform (sample_points)

        ''' Interpolate sample points to generate transformed image '''
        img = np.zeros([Nx, Ny])
        for i in range(Nx * Ny):
            point = original_points[i]
            img[i % Nx, int(math.floor(i / Nx))] = self.interpolate(image, point)
            
        return img;

    def interpolate(self, image, point):

        Ny = image.shape[0]
        Nx = image.shape[1]

        ''' Convert point from normalized pixel to actual pixel in image '''
        orig_col = 0.5 * (point.x + 1) * (Nx - 1) 
        orig_row = 0.5 * (point.y + 1) * (Ny - 1)

        ''' Find nearest pixels '''
        row_ceil = int(math.ceil(orig_row))
        col_ceil = int(math.ceil(orig_col))
        if row_ceil == orig_row:
            row_ceil = int(orig_row + 1)
        if col_ceil == orig_col:
            col_ceil = int(orig_col + 1)
        row_floor = int(math.floor(orig_row))
        col_floor = int(math.floor(orig_col))

        ''' Handle boundaries '''
        row_floor_index = Ny - 1 if row_floor >= Ny else row_floor
        row_ceil_index = Ny - 1 if row_ceil >= Ny else row_ceil
        col_floor_index = Nx - 1 if col_floor >= Nx else col_floor
        col_ceil_index = Nx - 1 if col_ceil >= Nx else col_ceil
        row_floor_index = 0 if row_floor < 0 else row_floor_index
        row_ceil_index = 0 if row_ceil < 0 else row_ceil_index   
        col_floor_index = 0 if col_floor < 0 else col_floor_index
        col_ceil_index = 0 if col_ceil < 0 else col_ceil_index

        ''' Bilinear Interpolate '''
        val = ((orig_row - row_floor) * (orig_col - col_floor) * image[row_ceil_index, col_ceil_index]) + \
                ((row_ceil - orig_row) * (orig_col - col_floor) * image[row_floor_index, col_ceil_index]) + \
                ((orig_row - row_floor) * (col_ceil - orig_col) * image[row_ceil_index, col_floor_index]) + \
                ((row_ceil - orig_row) * (col_ceil - orig_col) * image[row_floor_index, col_floor_index])
        return val

Sample = Sample()
