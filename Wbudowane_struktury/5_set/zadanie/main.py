from shop.delivery import products_delivery


def run_homework():
    # products = products_delivery()
    # print(products)

    needed_products = [
        "chleb",
        "ciastka",
        "jabłka",
        "dżem",
        "pomarańcze",
        "marchew",
        "bułki",
        "ziemniaki",
        "ser",
        "mleko"
    ]
    received_products = []

    while not set(needed_products) == set(received_products):
        new_products = products_delivery()
        received_products += new_products
        print(f"Otrzymano: {new_products}")
        missing_products = set(needed_products).difference(received_products)
        print(f"Brakuje jeszcze: {missing_products}")

    print(f"Otrzymano: {received_products}")


if __name__ == '__main__':
    run_homework()