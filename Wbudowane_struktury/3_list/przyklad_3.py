# list comprehensions
def run():
    # numbers = [number for number in range(15)]
    # print(numbers)

    numbers = [number for number in range(15) if number % 2 == 0]
    print(numbers)

    favourite_flavours = ["malinowy", "truskawkowy", "czekoladowy", "pistacjowy", "kokosowy"]
    # flavours = [flavour for index, flavour in enumerate(favourite_flavours) if index % 2 == 0]
    # print(flavours)

    flavours = [flavour if index % 2 == 0 else "-----" for index, flavour in enumerate(favourite_flavours)]
    print(flavours)


if __name__ == '__main__':
    run()