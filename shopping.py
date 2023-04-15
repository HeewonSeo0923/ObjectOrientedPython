from hw01_answer import Product, ShoppingCart


products = [Product('제주 삼다수 그린 2L', 1200, 5),
            Product('신라면(120g*5입)', 4100, 2),
            Product('CJ 햇반(210g*12입)', 13980, 1),
            Product('몽쉘크림(12입)', 4780, 1)]

for product in products:
    print(f"{product} ----> {product.get_price():6d}")

my_cart = ShoppingCart()

for p in products:
    my_cart.add(p)

print(my_cart)
print()
print('** 전체 영수증 입력 확인 **')
my_cart.billing()
print()
my_cart.delete(products[3], 1)
print('** 몽쉘삭제된 영수증 **')
my_cart.billing()
print()
print('** 구운감자 추가 영수증 **')
my_cart.add(Product('해태 구운감자(135g*5입)', 3580, 2))
my_cart.billing()
