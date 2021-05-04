def run():
    try:
        print("Przed wyrzuceniem wyjątku")
        raise TypeError("Coś poszło nie tak")
        print("To się nie wydarzy")
    except TypeError as error:
        print(f"Wyjątek złapany - zawiera informację: {error}")

    print("Program działa dalej")


if __name__ == '__main__':
    run()