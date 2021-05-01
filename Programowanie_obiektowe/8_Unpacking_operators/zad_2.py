def wypisz_str(**kwargs):
    napis = ""
    for argument_name, argument_value in kwargs.items():
        napis += f"{argument_name} = {argument_value} "
    print(napis)


def run():
    wypisz_str(first_name="Mariusz", age=26)


if __name__ == "__main__":
    run()