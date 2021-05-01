import math


def run():
    print(round(2.7))

    print(round(1.5))
    print(round(2.5))

    print(round(3.129, ndigits=2))

    # funkcja floor(podłoga)
    print(math.floor(2.8))
    print(math.floor(1.2))
    print(math.floor(-1.3))

    # funkcja ceil(sufit)
    print(math.ceil(3.6))
    print(math.ceil(1.1))
    print(math.ceil(-1.1))

    # Rzutowanie na int

    print(int(1.1))
    print(int(1.9999))
    print(int(1.99999999999999999999))
    print(math.floor(1.99999999999999999999))


if __name__ == '__main__':
    run()

