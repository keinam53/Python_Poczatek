class Product:

    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

    def print_self(self):
        print(f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price}/szt")