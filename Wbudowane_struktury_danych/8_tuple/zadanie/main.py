from shop.product import Product


def test_product_eq():
    parameters = [
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 4, True),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 5, False),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Rozrywka", 4, False),
        ("Ciastka", "Jedzenie", 4, "Piwo", "Jedzenie", 4, False)
    ]

    for params in parameters:
        name, category_name, price, other_name, other_category_name, other_price, expected_result = params

        result = Product(name, category_name, price) == Product(other_name, other_category_name, other_price)
        if result == expected_result:
            print("OK")
        else:
            print(f"Błąc! Dla danych {params} wynik: {result} powinien być: {expected_result}")


def run():
    test_product_eq()


if __name__ == '__main__':
    run()

