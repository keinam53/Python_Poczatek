
from shop.Product import Expire


def run():
    product = Expire("Ciastka", "Jedzenie", 7, 2020, 2)
    product.does_expire(2021)
    product.does_expire(2023)
    product.does_expire(2010)


if __name__ == '__main__':
    run()