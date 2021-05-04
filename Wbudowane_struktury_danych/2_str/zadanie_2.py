def print_format():
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    first_name = first_name.strip()
    last_name = last_name.strip()

    print("Nazywasz się {} {} - miło Cię poznać".format(first_name, last_name))


def print_proc():
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    first_name = first_name.strip()
    last_name = last_name.strip()

    print("Nazywasz się %(imie)s %(nazwisko)s - miło mi" %{"imie": first_name, "nazwisko": last_name})


if __name__ == '__main__':
    # print_format()
    print_proc()
