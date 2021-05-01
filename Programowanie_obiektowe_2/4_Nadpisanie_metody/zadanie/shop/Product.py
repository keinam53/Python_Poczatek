class Product:

    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price}/szt"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
               self.category_name == other.category_name and
               self.unit_price == other.unit_price)


class Expire(Product):
    def __init__(self, name, category_name, unit_price, year_of_production, period_of_validity):
        super().__init__(name, category_name, unit_price)
        self.period_of_validity = period_of_validity
        self.year_of_production = year_of_production

    def does_expire(self, current_year):
        time = current_year - self.year_of_production
        if time < 0:
            print("Data produkcji póżniejsza niż dzisiejsza")
        elif time < self.period_of_validity:
            print("Produkt ok")
        else:
            print("Produkt nok")
