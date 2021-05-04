def run():
    print("Hello")
    raise Exception("To błąd")
    print("To się nie wypisze")


if __name__ == '__main__':
    run()