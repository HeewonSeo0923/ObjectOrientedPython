import math
def cal_area(r) :
    area = math.pi * r * r
    return area

if __name__ == '__main__':
    radius = float(input("원의 반지름 : "))
    area = cal_area(radius)

    print(f'원의 반지름 : {radius:.3f}')
    print(f'원의 면적: {area:.3f}')