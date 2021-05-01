def zamiana_na_napis(*args):
    result = ""
    for element in args:
        result += str(element)
        result += "-"
    return result[:-1]


def run():
    napis = zamiana_na_napis(1, 4, "LOL", 0, ":)")
    print(napis)


if __name__ == '__main__':
    run()