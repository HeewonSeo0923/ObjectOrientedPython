import math

class Circle :
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        area = math.pi * math.pow(self.radius, 2)
        return area

if __name__ == '__main__':
    radius = float(input('원의 반지름 : '))
    circle = Circle(radius)
    area = circle.cal_area()

    print(f'원의 반지름 : {circle.radius:.3f}')
    print(f'원의 면적: {circle.cal_area():.3f}')