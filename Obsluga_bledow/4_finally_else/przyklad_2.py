class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("To nie liczba")

    if number % 2 != 0:
        raise NumberParsingError("Liczba nie jest parzysta")

    return number / 2


def run():
    number_str = input("Podaj liczbę: ")

    try:
        parsed_number = handle_even_number(number_str)
    except NumberParsingError as error:
        print(error)
    else:
        result = 100 / parsed_number
        print(f"Wynik działania wynosi: {result}")
    finally:
        print("Koniec programu")


if __name__ == '__main__':
    run()
