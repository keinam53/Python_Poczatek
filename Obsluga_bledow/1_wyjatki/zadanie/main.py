from shop.data_generator import generate_order_elements, generate_product, generate_quantity
from shop.order import Order


def run():
    # order_elements_on_limit = generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    # order_on_limit = Order("Mariusz", "Baran", order_elements=order_elements_on_limit)
    # print(order_on_limit)
    #
    # product = generate_product()
    # quantity = generate_quantity()
    # order_on_limit.add_product_to_order(product, quantity)

    order_elements_over_limit = generate_order_elements(products_to_generate=Order.MAX_ELEMENTS + 1)
    order_over_limit = Order("Mariusz", "Baran", order_elements=order_elements_over_limit)
    print(order_over_limit)


if __name__ == '__main__':
    run()

