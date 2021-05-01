from shop.Express_order import ExpressOrder
from shop.data_generator import generate_order_elements


def run():
    order_elements = generate_order_elements()
    express_order = ExpressOrder("Mariusz", "Baran", "07-05-2021", order_elements)
    print(express_order)


if __name__ == '__main__':
    run()