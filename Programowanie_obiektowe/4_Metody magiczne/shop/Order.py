import random

from shop.order_element import OrderElement
from shop.Product import Product


class Order:

    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.calculate_price()
        return total_price

    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        product_details = "Zamówione produkty:\n"
        for element in self.order_elements:
            product_details = product_details + "\t" + f"{element}" + "\n"

        result = "\n".join([mark_line, order_details, value_details, product_details])
        return result

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False
        if len(self.order_elements) != len(other.order_elements):
            return False
        for order_element in self.order_elements:
            if order_element not in other.order_elements:
                return False
        return True


def generate_order():
    number_of_product = random.randint(1, 10)
    order_elements = []
    for product_number in range(number_of_product):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))

    order = Order(client_first_name="Mariusz", client_last_name="Baran", order_elements=order_elements)
    return order

