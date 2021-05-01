from shop.data_generator import generate_order_elements
from shop.order import Order


def run():
    order_elements = generate_order_elements()
    my_order = Order("Mariusz", "Baran", order_elements)
    print(my_order)


if __name__ == '__main__':
    run()

