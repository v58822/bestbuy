class Store:
    def __init__(self, products):
        """Initialize the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Return total quantity of all products in store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Return all active products in the store."""
        active = []
        for product in self.products:
            if product.is_active():
                active.append(product)
        return active

    def order(self, shopping_list):
        """Process an order (list of (product, amount)) and return total price."""
        total = 0
        for product, amount in shopping_list:
            price = product.buy(amount)
            total = total + price
        return total
