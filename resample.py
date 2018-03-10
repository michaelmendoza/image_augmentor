import numpy as np
import math
import time

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

Resample = Resample()