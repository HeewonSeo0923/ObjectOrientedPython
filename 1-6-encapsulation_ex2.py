class A :
    def __init__(self, x = 0):
        self.__x = x                          # encapsulation

if __name__ == '__main__':
    a = A()
    b = A(10)

    print(f'객체 a의 속성값 x : {a.x:.1f}')

    a.x = 2*b.x
    print(f'객체 a의 속성값 x : {a.x:.1f}')
    print(f'객체 b의 속성값 x : {b.x:.1f}')