def handle_even_number(number):
    try:
        if number % 2 != 0:
            raise ValueError("Liczba nieparzysta")
    except TypeError as error:
        print(f"Błąd związany z typem: {error}")
        raise error

    print(f"Liczba podzielona przez 2 wynosi  {number / 2}")


def run():
    number = input("Podaj liczbę: ")
    if number.isnumeric():
        number = int(number)

    try:
        handle_even_number(number)
    except ValueError as error:
        print(f"Zła wartość: {error}")
    except TypeError as error:
        print(f"Zły typ: {error}")


if __name__ == '__main__':
    run()
