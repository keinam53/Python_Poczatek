from shop.Order import Order
from shop.data_generator import generate_order_elements


def run():
    first_name = "Mariusz"
    last_name = "Baran"
    order = generate_order_elements()
    zamowienie = Order(first_name, last_name, order)

    #ZAD 1
    # for elements in order_elements:
    #     print(elements)
    # ZAD 2 i 3
    print(zamowienie)
    new_order = generate_order_elements(1)
    zamowienie.order_elements = new_order
    print(zamowienie)

    too_many_order = generate_order_elements(8)
    zamowienie.order_elements = too_many_order
    print(zamowienie)
    print(zamowienie.total_price)




if __name__ == '__main__':
    run()