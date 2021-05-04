def run():
    favourite_flavours = ["malinowy", "truskawkowy", "czekoladowy", "pistacjowy", "kokosowy"]
    print(favourite_flavours)

    # clear usuwa wszystko z listy
    favourite_flavours.clear()
    print(favourite_flavours)

    # reverse odwraca
    favourite_flavours.reverse()
    print(favourite_flavours)

    # count liczy wystąpienia
    print(favourite_flavours.count("malinowy"))

    # copy = kopia listy
    copy_favourite_flovers = favourite_flavours.copy()
    print(copy_favourite_flovers)

    # extend łączy 2 listy
    new_flavours = ["orzechowy", "jagodowy"]
    favourite_flavours.extend(new_flavours)
    print(favourite_flavours)

    # new_flavours = ["orzechowy", "jagodowy"]
    # favourite_flavours += new_flavours
    # print(favourite_flovers)

    # mnożenie list *
    two_flavours = ["orzechowy", "jagodowy"]
    print(two_flavours * 4)


if __name__ == '__main__':
    run()