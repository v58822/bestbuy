from store import Store
from products import Product

LINE_SEPARATOR_STORE = "-" * 55
LINE_SEPARATOR_MENU = "-" * 30
MENU_CENTER = 30


def make_order(store):
    """Build a shopping list from user input and call store.order()."""
    available_products = store.get_all_products()
    shopping_list = []

    print(LINE_SEPARATOR_STORE)
    for i, product in enumerate(available_products, start=1):
        print(f"{i}. {product.show()}")
    print(LINE_SEPARATOR_STORE)
    print("When you want to finish order, enter empty text.")

    while True:
        # Ask for product number
        product_input = input("Which product # do you want? ")
        if product_input == "":
            break

        # Validate product number
        try:
            product_index = int(product_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not (1 <= product_index <= len(available_products)):
            print("Invalid product number.")
            continue

        # Ask for amount
        amount_input = input("What amount do you want? ")
        try:
            amount = int(amount_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount <= 0:
            print("Amount must be positive.")
            continue

        # Add to shopping list
        product = available_products[product_index - 1]
        shopping_list.append((product, amount))
        print("Product added to list!\n")

    if shopping_list:
        try:
            total = store.order(shopping_list)
        except ValueError as e:
            print(f"Order failed: {e}")
            return
        print("********")
        print(f"Order made! Total payment: ${total}")


def get_menu_choice(max_choice):
    """Prompts the user to choose a valid menu option between 1 and max_choice."""
    while True:
        try:
            choice = int(input(f"Enter choice (1–{max_choice}): "))
            print()
            if 1 <= choice <= max_choice:
                return choice
            print(f"Number must be between 1 and {max_choice}.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function: initializes the store, displays the menu, and handles user actions."""
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)

    menu_items = [
        "List all products in store",
        "Show total amount in store",
        "Make an order",
        "Quit"
    ]

    while True:
        print(LINE_SEPARATOR_MENU)
        print("Store Menu".center(MENU_CENTER))
        print(LINE_SEPARATOR_MENU)
        for i, item in enumerate(menu_items, start=1):
            print(f"{i}. {item}")

        choice = get_menu_choice(len(menu_items))

        if choice == 1:
            print(LINE_SEPARATOR_STORE)
            for product in best_buy.get_all_products():
                print(product.show())
            print(LINE_SEPARATOR_STORE)
            print()
        elif choice == 2:
            print(f"Total of {best_buy.get_total_quantity()} items in store")
            print()
        elif choice == 3:
            make_order(best_buy)
            print()
        elif choice == 4:
            break


if __name__ == "__main__":
    main()
