import random
from shop.Product import Product
from shop.order_element import OrderElement
from shop.Order import Order


MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_QUANTITY = 1
MAX_QUANTITY = 10


def generate_order_elements(number_of_products=None):
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ELEMENTS)
    order_elements = []
    for product_number in range(number_of_products):
        name = f"Produkt {product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        produkt = Product(name, category_name, unit_price)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(produkt, quantity))
    return order_elements

