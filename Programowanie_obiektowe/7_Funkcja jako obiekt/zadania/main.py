from shop.Order import Order
import random
from shop.Product import Product
from shop.order_element import OrderElement
from shop.discount_policy import christmas_policy, loyal_customer_policy


def run():
    abc = []
    for i in range(5):
        abc.append(Order.generate_order(random.randint(1, 5)))

    abc.sort(key=lambda qwe: qwe.total_price)
    for qwe in abc:
        print(qwe)


# def generate_order_elements():
#     order_elements = []
#     for product_number in range(5):
#         name = f"Produkt {product_number}"
#         category_name = "Inne"
#         unit_price = random.randint(1, 30)
#         produkt = Product(name, category_name, unit_price)
#         quantity = random.randint(1, 10)
#         order_elements.append(OrderElement(produkt, quantity))
#     return order_elements
#
#
# def run():
#     first_name = "Mariusz"
#     last_name = "Baran"
#     order_elements = generate_order_elements()
#     normal_order = Order(first_name, last_name, order_elements)
#     loyal_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
#     christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)
#     print(normal_order)
#     print(loyal_order)
#     print(christmas_order)



if __name__ == '__main__':
    run()