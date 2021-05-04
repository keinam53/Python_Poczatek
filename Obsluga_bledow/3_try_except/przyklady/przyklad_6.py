class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("To nie liczba")

    if number % 2 != 0:
        raise NumberParsingError("Liczba nieparzysta")

    print(f"Liczba podzielona przez 2 wynosi  {number / 2}")


def run():
    number_str = input("Podaj liczbę: ")
    try:
        handle_even_number(number_str)
    except NumberParsingError as error:
        print(f"Komunikat o błędzie: {error}")


if __name__ == '__main__':
    run()
