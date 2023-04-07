class Product:
    def __init__(self, name: str, price: int, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self) -> int:
        money = self.price * self.quantity
        return money
    def __str__(self):
        info = f'{self.name}  {self.price}  {self.quantity}'
        return info

class ShoppingCart:
    def __init__(self):
        self.shop_list = []


    def __str__(self):
        info = f'구입 품목 :\n'

        for lists in self.shop_list:
            info += f'{lists}\n'
        return info

    def add(self, Product) -> None:
        self.shop_list.append(Product)

    def delete(self, qty) -> None:
        if qty.quantity == 0:
            self.shop_list.remove(qty)
        else:
            pass

    def total_price(self) -> int:
        return sum([product.get_price() for product in self.shop_list])


    def billing(self) -> str:
        total_price = 0
        print("구입 품목: ")
        for product in self.shop_list:
            item_price = product.get_price()
            print(f"{product.name}     {product.quantity}개    {item_price}")
            total_price += item_price
        print('------------------------------------')
        print(f"합계                         {total_price}")


if __name__ == "__main__" :
    my_cart = ShoppingCart()
    water = Product('제주 삼다수 그린 2L', 1200, 5)
    ramen = Product('신라면(120g*5입)', 4100, 2)
    bab = Product('CJ 햇반(210g*12입)', 13980, 1)
    bread = Product('몽쉘크림(12입)', 4780, 1)
    my_cart.add(water)
    my_cart.add(ramen)
    my_cart.add(bab)
    my_cart.add(bread)

    # 2 츨력
    print("** 과제 2번 출력 **")
    print(my_cart)

    # 몽쉘 삭제하기
    setattr(bread, 'quantity', 0)
    print()
    my_cart.delete(bread)
    print('** 과제 3번 출력 **')
    print('1. 몽쉘 삭제하기')
    print(my_cart)

    # 구운감자 추가
    potato = Product('해태구운감자(135g*5입)', 3580, 2)
    my_cart.add(potato)
    print()
    print('2. 구운감자 추가하기')
    print(my_cart)

    print()

    # 4번
    # 돈 계산하기
    print("** 과제 4번 출력 **")
    my_cart.billing()

