from colorama import Fore


class Product:
    quantity = 0

    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method. Creates the instance variables.
        If something is invalid, raises an exception.
        """
        try:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name should not be empty.")
            if price <= 0:
                raise ValueError("Price must be greater than 0.")
            if quantity < 0:
                raise ValueError("Quantity must be greater than 0.")
        except ValueError as e:
            print(f"Error initializing the following Product: {e}.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Getter function for quantity.
        Returns the quantity (float).
        """
        return float(self.quantity)

    def set_quantity(self, new_quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        if new_quantity >= 0:
            Product.quantity += new_quantity - self.quantity
            self.quantity = new_quantity
        else:
            self.deactivate()

    def is_active(self):
        """
        Getter function for active. Returns True if the product is active, otherwise False.
        """
        if self.active:
            return True
        else:
            return False

    def activate(self):
        """Activates the product"""
        print(Fore.CYAN + f"Internal Info: {self.name} has been activated." + Fore.RESET)
        self.active = True

    def deactivate(self):
        """Deactivates the product"""
        print(Fore.CYAN + f"Internal Info: {self.name} has been deactivated." + Fore.RESET)
        self.active = False

    def show(self):
        """Returns a string that represents the product."""
        return f"The Product name is {self.name}, its price is {self.price} and it has a quantity of {self.quantity}."

    def buy(self, quantity):
        """Buys a certain quantity of a product, returns the total price (float) of the purchase and
           updates the quantity of the product.
        """

        if not self.active:
            print(Fore.RED + f"Error: {self.name} has been deactivated and therefore can't be purchased." + Fore.RESET)
            return 0

        elif quantity > self.quantity:
            print(Fore.RED + f"Error: Not enough items of {self.name} in stock. Available quantity: {self.quantity}." + Fore.RESET)
            return 0

        elif quantity <= 0:
            print(Fore.RED + f"Error: Quantity must be greater than 0." + Fore.RESET)
            return 0

        total_price = float(quantity * self.price)
        self.quantity -= quantity

        print(
            f"You bought {quantity} pieces of {self.name}. The total price is {total_price} EUR. The remaining stock is {self.quantity}.")

        if self.quantity == 0:
            self.deactivate()
            print(Fore.CYAN + f"Internal Info: {self.name} is now out of stock." + Fore.RESET)

        return round(total_price, 2)

