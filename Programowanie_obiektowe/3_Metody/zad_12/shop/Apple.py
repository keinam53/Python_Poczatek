class Apple:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def calculate_price(self, quantity):
        price_kg = quantity * self.price
        return price_kg


