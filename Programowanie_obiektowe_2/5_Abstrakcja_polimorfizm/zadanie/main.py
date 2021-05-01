from shop.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
from shop.data_generator import generate_order_elements
from shop.Order import Order


def run():
    order_elements = generate_order_elements()
    no_discount = DiscountPolicy()
    proc_discount = PercentageDiscount(20)
    absolute_discount = AbsoluteDiscount(100)

    a = Order("M", "B", order_elements, no_discount)
    print(a)
    b = Order("M", "B", order_elements, proc_discount)
    print(b)
    c = Order("M", "B", order_elements, absolute_discount)
    print(c)


if __name__ == '__main__':
    run()