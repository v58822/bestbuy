from products import Product


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """ returns all products which are active """
        active = []
        for product in self.products:
            if product.is_active():
                active.append(product)
        return active

    def order(self, shopping_list):
        total = 0
        for product, amount in shopping_list:
            price = product.buy(amount)
            total = total + price
        return total

    def show_all_products(self):
        for product in self.get_all_products():
            out = product.show()
            if out is not None:
                print(out)


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()
