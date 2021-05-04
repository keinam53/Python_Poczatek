import random


def add_numbers_set(numbers):
    number = random.randint(0, 10)
    numbers.add(number)
    return numbers


def add_numbers_frozenset(numbers):
    number = random.randint(0, 10)
    return numbers.union({number})


def run():
    # numbers = set()
    numbers = frozenset()

    while len(numbers) < 11:
        print(numbers)

        # numbers = add_numbers_set(numbers)
        numbers = add_numbers_frozenset(numbers)
    print(numbers)


def run_remember():
    numbers = frozenset()
    result = []
    while len(numbers) < 11:
        result.append(numbers)
        numbers = add_numbers_frozenset(numbers)
    print(result)


if __name__ == "__main__":
    # run()
    run_remember()