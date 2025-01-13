class Product:
    def __init__(self, name: str, price: float, quantity: int):
        # Validate inputs
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> float:
        return float(self.quantity)


    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        if self.active:
            return True
        else:
            return False


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        try:
            if self.quantity > quantity:
                self.quantity -= quantity
                return self.price * quantity
            if self.quantity == quantity:
                self.quantity = 0
                self.deactivate()
                return self.price * quantity
            raise ValueError("Insufficient quantity")
        except ValueError as e:
            print(e)
