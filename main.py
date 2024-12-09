from products import Product
from store import Store


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.show())
    print(mac.show())

    bose.set_quantity(100)
    mac.set_quantity(100)

    print(bose.show())
    print(mac.show())

    bose.buy(100)
    mac.buy(7)

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    active_products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()