class Circle:
    def __init__(self, radius:float, ctr_pt:"Point"=Point()):
        self._radius = radius
        self._center_pt = ctr_pt

    @property
    def radius(self):
        return  self._radius

    @radius.setter
    def radius(self, radius):
        return self._radius = radius

    @property
    def center_pt(self):
        return self._center_pt

    @center_pt.setter
    def center_pt(self, ctr_pt):
        return self._center_pt = ctr_pt

    @property
    def area(self):
        return math.pi * math.pow(self._radius,2)

    def move_center(self, ctr_pt):
        self._center_pt = ctr_pt

if __name__ == '__main__':
    c = Circle(2.0, Point())
