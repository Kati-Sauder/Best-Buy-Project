from products import Product


class Store:

    def __init__(self, product_list=None):
        """
        Initiator (constructor) method. Creates the instance variables.
        If something is invalid, raises an exception.
        """
        if product_list:
            self.product_list = product_list
        else:
            self.product_list = []

    def add_product(self, product):
        """
        Adds a product to the Store.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a product from the Store.
        """
        self.product_list.remove(product)

    def get_total_quantity(self):
        """
        Returns how many items are in the store in total. --> int
        """
        total_quantity = sum(product.quantity for product in self.product_list)
        return total_quantity

    def get_all_products(self):
        """
        Returns all products in the store that are active. --> List of products
        """
        active_products = [product for product in self.product_list if product.active]
        return active_products

    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
active_products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(active_products[1], 13), (active_products[2], 24)]))
print(store.get_total_quantity())

