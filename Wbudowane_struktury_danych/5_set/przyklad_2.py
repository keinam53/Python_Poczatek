import random


def run():
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    my_favourite_flavours = set(flavours)
    print(my_favourite_flavours)

    your_favourite_flavours = {"Orzechowy", "Pistacjowy", "Truskawkowy"}
    print(your_favourite_flavours)

    # union - suma zbiorów
    all_flavours = my_favourite_flavours.union(your_favourite_flavours)
    print(all_flavours)

    # intersection - część wspólna
    common_flavours = my_favourite_flavours.intersection(your_favourite_flavours)
    print(common_flavours)

    # difference - różnica zbiorów
    only_mine_flavours = my_favourite_flavours.difference(your_favourite_flavours)
    print(only_mine_flavours)

    # issubset - sprawdzenie czy zbiór jest podzbiorem innego
    print(my_favourite_flavours.issubset(all_flavours))

    # usuwanie duplikatów
    numbers = [random.randint(0, 40) for _ in range(60)]
    print(numbers)
    no_duplicate = set(numbers)
    print(no_duplicate)

    # sprawdzenie czy dana lista zawiera podane elementy
    digits = set(number for number in range(10))
    print(f"Czy udało się wylosować wszystkie liczby 0 - 10? {digits.issubset(no_duplicate)}")


if __name__ == '__main__':
    run()
