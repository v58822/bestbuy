class Product:
    def __init__(self, name: str, price: float, quantity: int):

        if name == "" or name is None:
            raise ValueError("Name can not be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise ValueError("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False

        return self.price * quantity


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

bose.set_quantity(1000)
print(bose.show())
