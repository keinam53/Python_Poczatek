import random
from shop.Product import Product


class Order:

    MAX_ORDER_NUMBER = 20

    def __init__(self, client_first_name, client_last_name, products=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if products is None:
            products = []
        self.products = products
        total_price = 0
        for product in products:
            total_price = total_price + product.unit_price
        self.total_price = total_price

    def print_self(self):
        print("=" * 20)
        print(f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}")
        print(f"Wartość zamówienia: {self.total_price} PLN")
        print("Zamówione produkty:")
        for product in self.products:
            print("\t", end="")
            product.print_self()
        print("=" * 20)
        print()


def generate_order():
    number_of_products = random.randint(1, 20)
    products = []
    for product_number in range(number_of_products):
        product_name = f"Produkt - {product_number + 1}"
        category = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category, unit_price)
        products.append(product)

    order = Order("Mariusz", "Baran", products)
    return order


