def run():
    # krotka jest immutable!!!
    human_info = "Mariusz", "Baran", 26
    print(human_info)

    human_info = ("Mariusz", "Baran", 26)
    print(human_info)

    # odwołanie do elementu za pomocą indeksu
    print(human_info[0])
    print(human_info[1])
    print(human_info[2])
    print(len(human_info))

    # krotka może mieć 1 element
    something = ("Mariusz",)
    print(something)

    # pusta krotka
    empty_tuple = ()
    print(empty_tuple)
    empty_tuple = tuple()
    print(empty_tuple)

    #zamiana listy na krotkę
    numbers = [1, 2, 3, 4]
    tuple_numbers = tuple(numbers)
    print(tuple_numbers)

    # można iterować
    for number in tuple_numbers:
        print(number)


if __name__ == '__main__':
    run()