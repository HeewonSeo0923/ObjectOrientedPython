import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0.0, 0.0)

    def cal_dist(self, other):
        d = math.hypot(self.x-other.x, self.y-other.y)
        return d

if __name__ == '__main__':
    p0 = Point()
    p1 = Point(1.0, 1.0)
    print(f'Distance from p0 to p1 : {p0.cal_dist(p1):.3f}')