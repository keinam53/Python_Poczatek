class NumberParsingError(Exception):
    pass


def handle_even_number(number):
    try:
        if number % 2 != 0:
            raise NumberParsingError("Liczba nieparzysta")
    except TypeError:
        raise NumberParsingError("To nie iczba")

    print(f"Liczba podzielona przez 2 wynosi  {number / 2}")


def run():
    number = input("Podaj liczbę: ")
    if number.isnumeric():
        number = int(number)

    try:
        handle_even_number(number)
    except NumberParsingError as error:
        print(f"Komunikat o błędzie: {error}")


if __name__ == '__main__':
    run()
