class Apple:

    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def calculate_price(self, quantity):
        return quantity * self.price

    def __repr__(self):
        return f"Odmiana jabłka: {self.species_name} | Rozmiar: {self.size} | Cena: {self.price}"