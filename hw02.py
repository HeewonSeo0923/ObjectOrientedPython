class Product:
    discount_rate:float = 0
    def __init__(self, name : str, price: int, quantity: int):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self) -> int:
        return self.price * self.quantity * (1 - Product.discount_rate * 0.01)

    def __str__(self):
        return f'{self.name:25s}\t{self.price:5d}원{self.quantity:3d}개'


class ShoppingCart:
    def __init__(self):
        self.__shop_list = []

    @property
    def shop_list(self):
        return self.__shop_list

    def add(self, pdt) -> None:
        self.shop_list.append(pdt)

    def delete(self, pdt, qty) -> None:
        updated = False
        for p in self.shop_list:
            if p.name == pdt.name:
                p.quantity -= qty
                updated = True
                if p.quantity <= 0:
                    self.shop_list.remove(p)
                break
        return updated

    def total_price(self) -> int:
        sum = 0
        for p in self.shop_list:
            sum += p.get_price()
        return sum

    def billing(self) -> str:
        print("구입 품목\n")

        for p in self.shop_list:
            print(f'{p}\t{p.get_price()}원')
        print(f"{58 * '-'}")
        print(f'{"합계":46s}{self.total_price()}원')

    def __str__(self):
        shop = ''
        for p in self.shop_list:
            shop += f'{p}\n'
        return shop


if __name__ == "__main__":
    # 물품 리스트 생성
    products = [Product('제주 삼다수 그린 2L', 1200, 5),
                Product('신라면(120g*5입)', 4100, 2),
                Product('CJ 햇반(210g*12입)', 13980, 1),
                Product('몽쉘크림(12입)', 4780, 1)]

    # 쇼핑카트 생성
    my_cart = ShoppingCart()

    # 물건 집어넣기
    for p in products:
        my_cart.add(p)

    print("** 2번문제 출력 **")
    print(f'{my_cart}\n')

    my_cart.delete(products[3], 1)
    print("** 몽쉘 삭제 **")
    print(f'{my_cart}\n')

    my_cart.add(Product('해태 구운감자(135g*5입)', 3580, 2))
    print("** 구운감자 추가 **")
    print(f'{my_cart}\n')

    # 4번 설정
    Product.discount_rate = 10

    # 5번 출력
    print("** 5번 출력 **")
    my_cart.billing()







