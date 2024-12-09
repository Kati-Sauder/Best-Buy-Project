from products import Product


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


if __name__ == "__main__":
    main()