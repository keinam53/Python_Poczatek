from dataclasses import dataclass
from enum import Enum


class ProductCategory(Enum):
    JEDZENIE = "JEDZENIE"
    INNE = "INNE"
    NARZEDZIA = "NARZEDZIA"

@dataclass
class Product:
    name: str
    category_name: ProductCategory
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name.value} | Cena: {self.unit_price} PLN/szt"


@dataclass
class ExpiringProduct(Product):
    production_year: int
    validity_years: int

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years
