def run():
    list_one = [number for number in range(1, 31) if number % 3 == 0]
    list_two = [number for number in range(1, 31) if number % 5 == 0]
    print(list_one)
    print(list_two)

    list_three = list_one + list_two
    print(list_three)


def print_sports():
    sports = []
    while True:
        sport = input("Podaj ulubiony sport lub zakończ X: ")
        if sport == "X":
            break
        sports.append(sport)
    print(sports[1::2])


if __name__ == '__main__':
    # run()
    print_sports()