from products import Product
from colorama import Fore


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

    def find_product(self, name):
        """
        Find and return a product instance by name.
        """
        for product in self.product_list:
            if product.name.lower() == name.lower():
                return product
        return None

    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            customer_purchase = product.buy(quantity)
            if customer_purchase is not None and customer_purchase > 0:
                total_price += customer_purchase
            else:
                print(Fore.RED + "Order failed." + Fore.RESET)

        if total_price > 0:
            total_price = round(total_price, 2)

            return float(total_price)
        else:
            return 0




