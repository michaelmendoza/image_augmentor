import numpy as np
import math
import time

from point import Point

class Resample:

    def warp(self, warp_image_view, image, transform):
        ''' Warps an image using a transform. The Point class is essential to this function. The point class 
        consists of an x,y pair that exists in the warped image, a u,v pair that exists in the original image,
        and the value of both of those locations. The list of Points is initialized with the x,y pairs of the warped 
        image, then inversely transformed to get the u,v pairs. Each u,v pair is interpolated against the original
        image, and that value is stored with the u,v pair and the x,y pair. Then the image is that value at each 
        x,y location.

        Args:
            warp_image_view:    dimensions of the resulting image, [x, y]
            image :             original image to be warped
            transform:          transform to be used when warping

        Return:
            an image that has been transformed and resampled
        '''

        # Initialize all the Point objects with the x,y of the warped image
        points = []
        for r in range(warp_image_view[1]):
            for c in range(warp_image_view[0]):
                points.append(Point(x=c,y=r))

        # Perform the inverse transform with the x,y pairs to get u,v points of the original image
        original_points = transform.inverse_transform(points);
        for i in range(len(original_points)):
            points[i].u = original_points[i][0]
            points[i].v = original_points[i][1]

        # Interpolate the u,v points against the image if they are within the window and then return that
        #   interpolation at each x,y location
        warped_image = np.zeros([warp_image_view[0],warp_image_view[1]])
        for i in range(len(points) - 1):
            if points[i][0] >= warp_image_view[1] or \
                points[i][1] >= warp_image_view[0] or \
                points[i][3] < 0 or \
                points[i][4] < 0 or \
                points[i][3] >= image.shape[1] or \
                points[i][4] >= image.shape[0]:
                continue
            else:
                points[i][2] = self.interpolate([points[i][3],points[i][4]], image)
                warped_image[points[i][1], points[i][0]] = points[i][2]
        
        return warped_image


    def interpolate(self, point, image):
        ''' Assigns a value to a point given the image that it came from

        Args: 
            point:  a point consisting of [x,y] float values that exists between actual pixels of an image
            image: the image from which we will be interpolating the point

        Return:
            the value that should be assigned to the point
        '''

        num_rows = image.shape[0]
        num_cols = image.shape[1]
        orig_row = int(point[1])
        orig_col = int(point[0])
        row_ceil = int(math.ceil(orig_row))
        col_ceil = int(math.ceil(orig_col))
        if row_ceil == orig_row:
            row_ceil = orig_row + 1
        if col_ceil == orig_col:
            col_ceil = orig_col + 1
        if row_ceil >= num_rows:
            return 0
        if col_ceil >= num_cols:
            return 0
        row_floor = int(math.floor(orig_row))
        col_floor = int(math.floor(orig_col))

        val = ((orig_row - row_floor)*(orig_col - col_floor)*image[row_ceil, col_ceil]) + \
                ((row_ceil - orig_row)*(orig_col - col_floor)*image[row_floor, col_ceil]) + \
                ((orig_row - row_floor)*(col_ceil-orig_col)*image[row_ceil, col_floor]) + \
                ((row_ceil-orig_row)*(col_ceil-orig_col)*image[row_floor, col_floor])
        return val


Resample = Resample()