import math


class Point:
    '''
    2차원 평면 위의 점의좌표 표현
    '''
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        '''

        :param x:
        :param y:
        '''
        self.x = x
        self.y = y

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0.0, 0.0)

    def cal_dist(self, other) -> float:
        d = math.hypot(self.x - other.x, self.y - other.y)
        return d


if __name__ == '__main__':
    p0 = Point()
    p1 = Point(1.0, 1.0)
    print(f"Distance from p0 to p1 : {p0.cal_dist(p1):.3f}")

    p0.move(-1.0, 1.0)
    p1.reset()
    print(f"Distance from p0 to p1 : {p0.cal_dist(p1):.3f}")
