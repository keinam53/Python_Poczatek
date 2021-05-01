# def calculate_sum_list(numbers):
#     result = 0
#     for number in numbers:
#         result = result + number
#     return result
#
#
# def run():
#     numbers = [1, 2, 3, 4, 5, 6]
#     wynik = calculate_sum_list(numbers)
#     print(wynik)



def calculate_sum_arg(*args):
    result = 0
    for number in args:
        result = result + number
    return result


def run():
    wynik = calculate_sum_arg(1, 2, 3, 4, 5, 6)
    print(wynik)

if __name__ == '__main__':
    run()