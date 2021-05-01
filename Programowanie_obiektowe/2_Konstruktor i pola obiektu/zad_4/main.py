from shop.Order import generate_order
from shop.Order import print_order


def run():
    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)


if __name__ == "__main__":
    run()