from shop.orders import create_new_order


def run():
    print("Witamy w sklepie")
    product = input("Co chcesz kupić? ")
    ilosc = int(input("Ile? "))
    result = create_new_order(product, ilosc)
    print(result)


if __name__ == '__main__':
    run()

