from shop.Order import Order
from shop.discount_policy import christmas_policy, loyal_customer_policy
from shop.data_generator import generate_order_elements


def run():
    first_name = "Mariusz"
    last_name = "Baran"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    loyal_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
    christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)
    print(normal_order)
    print(loyal_order)
    print(christmas_order)


if __name__ == '__main__':
    run()