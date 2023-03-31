class Product:
    def __init__(self, name: str, price: int, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def price(self, price, quantity) -> int:
        money = price * quantity
        return money

class ShoppingCart:
    def __init__(self):
        self.shop_list = []

    def add(self, Product) -> None:
        