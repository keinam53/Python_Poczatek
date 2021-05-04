from dataclasses import dataclass


@dataclass
class Potato:
    species_name: str
    size: str
    price: float

    def calculate_price(self, quantity):
        return quantity * self.price

    def __repr__(self):
        return f"Odmiana ziemniaka:'{self.species_name}', rozmiar:{self.size}, cena:{self.price}"
