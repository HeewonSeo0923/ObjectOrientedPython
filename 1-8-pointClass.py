import math

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.__x = x
        self.__y = y

    @property
    def get_x(self) -> float:
        return self.__x

    @property
    def get_y(self) -> float:
        return self.__y

    @property
    def set_x(self, x=float) :
        self.__x = x

    @property
    def set_y(self, y=float):
        self.__y = y

    def move(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    def reset(self) -> None:
        self.move(0.0, 0.0)

    def cal_dist(self, other) -> float:
        d = math.hypot(self.__x-other.get_x(), self.__y-other.get_y())
        return d


