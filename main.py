import products
import store

bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)
"""
print(bose.buy(550))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

bose.set_quantity(1000)
print(bose.show())

store = store.Store([bose, mac])

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
store.add_product(pixel)
price = store.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")
"""

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

store = store.Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))