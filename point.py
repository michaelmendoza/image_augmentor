
class Point:

    def __init__(self, value = None, x = None, y = None, bounding_box = None):
        self.value = value
        self.x = x
        self.y = y

        ''' Normalize x, y points between (-1, 1) '''
        if(bounding_box != None):
            self.y = (x / (bounding_box[0] - 1)) * 2.0 - 1.0
            self.x = (y / (bounding_box[1] - 1)) * 2.0 - 1.0

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):
        return "Point( %.1g, %.1g )" % (self.x, self.y)
        