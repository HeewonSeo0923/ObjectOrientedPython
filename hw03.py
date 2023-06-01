class Product:
    discount_rate: float = 0.0

    def __init__(self, name: str, price: int, quantity: int):
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
        return int(self.price * self.quantity * (1 - Product.discount_rate ))

    def __str__(self):
        return f'{self.name:25s}\t{self.price:5d}원{self.quantity:3d}개'


class Sales_product(Product):
    rate:float = 0.2

    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)

    def get_price(self) -> int:
        return int(self.price * self.quantity * (1 - Sales_product.rate ))

class Clearance_Product(Product):
    rate:float = 0.5

    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)

    def get_price(self) -> int:
        return int(self.price * self.quantity * (1 - Clearance_Product.rate ))


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
        total = 0
        for p in self.shop_list:
            total += p.get_price()
        return total

    def billing(self) -> str:
        print("구입 품목: \n")
        print(f'{"품목":37s}{"수량":10s}{"정가":10s}{"판매가":10s}')
        print("-" * 70)
        for p in self.shop_list:
            total_price = p.price * p.quantity
            print(f'{p.name:29s}{p.quantity:5d}{total_price:10,d}원{p.get_price():10,d}원')
        print("-" * 70)
        print(f'{"합계":50s}{self.total_price():10,d}원')

    def __str__(self):
        cart_info = ''
        for p in self.shop_list:
            cart_info += f'{p.name:25s}\t{p.price:20d}원{p.quantity:3d}개 {p.__class__.__name__:10s}\n'
        return cart_info

if __name__ == "__main__":
    # 2번 문제 쇼핑카트 추가하기
    products = [Product('제주 삼다수 그린 2L', 1200, 5),
                Product('신라면(120g*5입)', 4100, 2),
                Sales_product('CJ 햇반(210g*12입)', 13980, 1),
                Clearance_Product('노스페이스 올라운드 폴로 NT7PN00B', 65000, 1)]

    # 쇼핑카트 생성
    my_cart = ShoppingCart()

    # 물건 집어넣기
    for p in products:
        my_cart.add(p)

    print("** 2번문제 출력 **")
    print(f'{my_cart} \n')

    print("** 3번문제 출력 **")
    my_cart.billing()

