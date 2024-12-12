from products import Product
from store import Store
from colorama import Fore


def start(store):
    """
    This function displays a menu. The user is being prompted to make a choice between 1 and 4.
    If the user chooses 1, all active products in the store are being displayed.
    If the user chooses 2, the total amount of all products in the store is being presented.
    If the user chooses 3, an order can be placed. The user is then prompted to enter the product names and their quantity.
    If the product(s) match(es) one of the products in the store, it's/they're being added to the shopping list and the
    order-method from the store-module is being called. The quantity of the chosen products is being updated accordingly.
    """
    while True:
        print("\n".join([
            "Store Menu",
            "___________",
            "1. List all products in store",
            "2. Show total amount in store",
            "3. Place an order",
            "4. Quit",
             ]))

        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            available_products = [product for product in store.get_all_products() if product.quantity > 0]
            if available_products:
                for product in available_products:
                    print(f"{product.name}, Price: {product.price}, Quantity: {product.quantity}")
            else:
                print(Fore.RED + "There are currently no products in stock." + Fore.RESET)
            print("------")

        elif choice == "2":
            print("------")
            print(f"Total items in store: {store.get_total_quantity()}")
            print("------")

        elif choice == "3":
            print("------")
            shopping_list = []
            while True:
                order_product_name = input("Which product do you want? ")
                try:
                    order_product_quantity = int(input("What amount do you want? "))
                    if order_product_quantity <= 0:
                        raise ValueError(Fore.RED + "Quantity must be greater than 0." + Fore. RESET)

                    product = store.find_product(order_product_name)
                    if product:
                        shopping_list.append((product, order_product_quantity))
                        print(f"Added {order_product_quantity} of {product.name} to your shopping list.")

                    else:
                        print(Fore.RED + "Product not found." + Fore.RESET)

                except ValueError as e:
                    print(Fore.RED + f"Invalid input: {e}" + Fore.RESET)
                    print("Please try again")
                    continue

                continue_order = input("Do you want to order more products (Y/N?: ").strip().lower()
                if continue_order != "y":
                    break

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    if total_price > 0:
                        print(Fore.GREEN + f"Order total is: {total_price} EUR" + Fore.RESET)
                    else:
                        print(Fore.RED + "No items in shopping cart." + Fore.RESET)
                except Exception as e:
                    print(Fore.RED + f"The order couldn't be executed: {e}" + Fore.RESET)
            else:
                print(Fore.RED + "No products were added to the shopping list." + Fore.RESET)
                print("------")

        elif choice == "4":
            print("Exiting the store. Please come again.")
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 4." + Fore.RESET)


def main():
    """
    This function provides a product list to the store and calls the start function, which contains the main logic and
    flow of the program.
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)

    start(store)


if __name__ == "__main__":
    main()

