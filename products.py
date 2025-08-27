class Product:
    """Represents a product in the store with name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a new product."""
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
        """Return the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        """
        Set the stock quantity. 
        If quantity is 0 → deactivate product.
        If quantity > 0 → activate product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if quantity == 0:
            self.active = False
        if quantity > 0:
            self.active = True

    def is_active(self):
        """Return True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buy a given quantity of the product.
        Decreases stock, deactivates product if stock reaches 0.
        """
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
