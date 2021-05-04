def ask_for_name():
    name = input("Podaj 3 pierwsze litery imienia: ")
    name_len = len(name)

    if name_len < 3:
        raise ValueError("Za mało liter")
    if name_len > 3:
        raise ValueError("Za dużo liter")
    return name


def run():
    try:
        name = ask_for_name()
    except ValueError as error:
        print(error)
    else:
        print(f"OK - podałeś {name}")
    finally:
        print("Koniec programu")


if __name__ == '__main__':
    run()
