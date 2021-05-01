def run():
    numbers = []
    for number in range(15):
        numbers.append(number)
    print(numbers)
    # print(numbers[:4])
    # print(numbers[8:])

    print(numbers[4: 10])

    print(numbers[4: 14: 3])


if __name__ == '__main__':
    run()