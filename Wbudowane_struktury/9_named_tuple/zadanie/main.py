from collections import namedtuple

Apple = namedtuple("Apple", ["species_name", "size", "price"])


def run():
    apple = Apple("Gala", "M", 2.5)
    print(apple.species_name)
    print(apple.size)
    print(apple.price)

    print(apple[0])
    print(apple[1])
    print(apple[2])

    for data in apple:
        print(data)


if __name__ == '__main__':
    run()

