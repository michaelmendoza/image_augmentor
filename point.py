
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
