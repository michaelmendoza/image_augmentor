import numpy as np
import math
import time

from point import Point

class Resample:

    def resample(self, image, mode = 'nearest_neighbor', sigma = 1, N = 2):
        """ Resample the input image to a coordinate grid
            Args:
                image:  list of points where each point is a list
        """
        y_vals = []
        x_vals = []
        for i in range(image.shape[0]):
            x_vals.append(image[i][0])
            y_vals.append(image[i][1])

        # Return image will be m x n pixels, m and n are the furthest right and down pixels in the input image
        m = int(math.ceil(max(x_vals) + 1))
        n = int(math.ceil(max(y_vals) + 1))

        if mode == 'nearest_neighbor':
            start = time.clock()
            finalImage = np.ones([m,n]) * -1 # initialize all pixels to -1

            # For each input pixel, assign it's value to the nearest output pixel
            for pix in image:
                if pix[0] < 0 or pix[1] < 0:
                    continue
                finalImage[math.floor(pix[0] + 0.5),math.floor(pix[1] + 0.5)] = pix[2]

            if len(finalImage[1]) == 1: # if all points are ouside viewable window
                print("error: No valid points")
                return np.array([[0]])

            # For any unassigned output pixels, assign to it the average of all the surrounding pixels
            for row in range(finalImage.shape[0]):
                for col in range(finalImage.shape[1]):
                    if finalImage[row, col] == -1:
                        finalImage[row, col] = self.average_surrounding_pix(finalImage, row, col)
            end = time.clock()
            print('time:', end - start)
            return finalImage

        elif mode == 'convolution':
            start = time.clock()
            finalImage = np.zeros([m,n])

            for input_pixel in image:
                # find nearest integer pixel
                nearest_pixel = [round(input_pixel[1]), round(input_pixel[0])]
                # find all neighboring integer pixels within a distance of N
                neighbors = self.find_neighbors(input_pixel, nearest_pixel, N, finalImage.shape[0], finalImage.shape[1])
                # for each of those neighbors, assign to the corresponding output image pixel the result of the gaussian function 
                for neighbor in neighbors:
                    distance = math.sqrt((neighbor[0] - neighbor[0])**2 + (input_pixel[1] - input_pixel[1])**2)
                    finalImage[neighbor[1],neighbor[0]] = finalImage[neighbor[1],neighbor[0]] + round((input_pixel[2]* (1./(2.*float(sigma))) * math.exp(-(distance**2)/(float(sigma)**2))))
            end = time.clock()
            print('time:', end - start)
            return finalImage

        else:
            print("error: Invalid mode")
            return np.array([[0]])

    def average_surrounding_pix(self, image, row, col):
        if row == 0 and col == 0: # top left corner
            return (image[row + 1, col] + image[row, col + 1]) / 2
        elif row == 0 and col == image.shape[1] - 1: # top right corner
            return (image[row + 1, col] + image[row, col - 1]) / 2
        elif row == image.shape[0] - 1 and col == 0: # bottom left corner
            return (image[row - 1, col] + image[row, col + 1]) / 2
        elif row == image.shape[0] - 1 and col == image.shape[1] - 1: # bottom right corner
            return (image[row - 1, col] + image[row, col - 1]) / 2
        elif row == 0: # top edge
            return (image[row + 1, col] + image[row, col - 1] + image[row, col + 1]) / 3
        elif row == image.shape[0] - 1: # bottom edge
            return (image[row - 1, col] + image[row, col - 1] + image[row, col + 1]) / 3
        elif col == 0: # left edge
            return (image[row + 1, col] + image[row - 1, col] + image[row, col + 1]) / 3
        elif col == image.shape[1] - 1: # right edge
            return (image[row + 1, col] + image[row, col - 1] + image[row - 1, col]) / 3
        else:   # everything not on the outside
            return (image[row, col - 1] + image[row + 1, col] + image[row - 1, col] + image[row, col + 1]) / 4

    def find_neighbors(self, original_point, point, n, num_rows, num_cols):
        neighbors = []
        for x in np.linspace(point[1]-n, point[1]+n, (2*n)+1):
            for y in np.linspace(point[0]-n, point[0]+n, (2*n)+1):
                if np.all([math.sqrt((original_point[1] - y)**2 + ((original_point[0] - x)**2)) <= n,y < num_rows,x < num_cols]) :
                    neighbors.append([y, x])
        return neighbors

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


Resample = Resample()