
class Point:
    ''' Contains the value at the original image ([x,y]), which maps to the same value in the transformed image ([u,v])
        In other words, this Point represents the same location on an image before ([x,y]) and after ([u,v]) a transformation '''

    def __init__(self, value=-1, u=-1, v=-1, x=-1, y=-1):
        ''' Init Point '''
        self.value = value
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def __getitem__(self, num):
        ''' Allows the use of square brackets so points can be used in the transform functions
        
        example:
            Point[0] = Point.x
            Point[1] = Point.y
            Point[2] = Point.value
            Point[3] = Point.u
            Point[4] = Point.v

        '''
        if num == 0:
            return self.x
        elif num == 1:
            return self.y
        elif num == 2:
            return self.value
        elif num == 3:
            return self.u
        elif num == 4:
            return self.v
        else:
            return -1

    def __setitem__(self, num, item):
        ''' Allows the ability to set items with square brackets using the same logic as __getitem__ above
        '''
        if num == 0:
            self.x = item
        elif num == 1:
            self.y = item
        elif num == 2:
            self.value = item
        elif num == 3:
            self.u = item
        elif num == 4:
            self.v = item
        else:
            return -1

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.value) + " " + str(self.u) + " " + str(self.v)

        