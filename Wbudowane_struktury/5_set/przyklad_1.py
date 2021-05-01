def run():
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    my_favourite_flavours = set(flavours)
    print(my_favourite_flavours)

    your_favourite_flavours = {"Orzechowy", "Pistacjowy", "Kawowy"}
    print(your_favourite_flavours)

    # pusty zbiór
    empty_set = set()
    print(empty_set)
    print(type(empty_set))

    # add - dodawanie
    my_favourite_flavours.add("Gruszkowy")
    print(my_favourite_flavours)

    # remove = usuwa
    my_favourite_flavours.remove("Malinowy")
    print(my_favourite_flavours)
    #
    # # discard - usuwa bez błędu gdy nie ma takiego wpisu
    my_favourite_flavours.discard("Pistacjowy")
    print(my_favourite_flavours)

    # pop wyciąga element
    print(my_favourite_flavours.pop())

    # copy - kopia
    copy_my_favourite_flavours = my_favourite_flavours.copy()
    print(copy_my_favourite_flavours)
    copy_my_favourite_flavours.clear()
    print(copy_my_favourite_flavours)

    # update łączy zbiory
    all_flavours = my_favourite_flavours
    all_flavours.update(your_favourite_flavours)
    print(all_flavours)

    print(len(all_flavours))


if __name__ == '__main__':
    run()







