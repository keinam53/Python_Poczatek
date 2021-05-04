from shop import data_generator
from shop.order import Order
from shop.product import Product
from shop.errors import ElementsInOrderLimitError


def run_homework():
    order_elements = data_generator.generate_order_elements(Order.MAX_ELEMENTS)
    order_on_limit = Order("Mariusz", "Baran", order_elements)

    product = data_generator.generate_product()
    quantity = data_generator.generate_quantity()

    try:
        order_on_limit.add_product_to_order(product, quantity)
    except ElementsInOrderLimitError as error:
        print(f"{error}, dostępna ilość: {error.allowed_limit}")


if __name__ == '__main__':
    run_homework()
