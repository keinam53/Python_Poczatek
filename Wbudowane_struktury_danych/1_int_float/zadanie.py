import math
import random


def run():
    floats = []
    for _ in range(6):
        liczba_float = random.uniform(-20, 20)
        floats.append(liczba_float)
    print(floats)

    ints = []
    for _ in range(3):
        liczba_int = random.randint(1, 10)
        ints.append(liczba_int)
    print(ints)

    print(round(floats[0]))
    print(math.ceil(floats[1]))
    print(math.floor(floats[2]))

    print(floats[3] ** ints[0])
    print(pow(floats[4], ints[1]))
    print(math.pow(floats[5], ints[2]))


if __name__ == '__main__':
    run()