def calculate_sum_list(*args):
    result = 0
    for number in args:
        result = result + number
    return result


def add_two_numbers(first, second):
    return first + second


def run():
    numbers = [1, 2, 3, 4, 5, 6]
    wynik = calculate_sum_list(*numbers)
    print(wynik)

    two_numbers = [10, 30]
    result = add_two_numbers(*two_numbers)
    print(result)

    polaczona_lista = [*numbers, *two_numbers]
    print(polaczona_lista)

if __name__ == '__main__':
    run()