def say_hello(name):
    print(f"Hello {name}")


def calculate(a, b):
    return a + b


def run():
    hello = say_hello
    hello("Mariusz")

    calculation = calculate
    result = calculation(10, 20)
    print(result)


if __name__ == '__main__':
    run()


