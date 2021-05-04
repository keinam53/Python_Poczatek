class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("To nie liczba")

    if number % 2 != 0:
        raise NumberParsingError("Liczba nie jest parzysta")

    print(f"Liczba podzielona przez 2 wynosi: {number / 2}")


def run():
    number = input("Podaj liczbę: ")

    # try:
    #     handle_even_number(number)
    # finally:
    #     print("Błędu nie złapiemy ale wykonamy zawsze")
    try:
        handle_even_number(number)
    except NumberParsingError as error:
        print(error)
        raise error
    finally:
        print("Błędu nie złapiemy ale wykonamy zawsze")


if __name__ == '__main__':
    run()
