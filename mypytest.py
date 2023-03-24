import mypy

def odd(n : int) -> bool:
    return n % 2 != 0

if __name__ == '__main__':
    nums: list[int] = [5, 3.4, 'h']

    for n in nums :
        if odd(n):
            print('dd')
        else:
            print('dd')