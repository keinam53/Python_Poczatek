import random


def run():
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")

    print(f"Nazywasz się {first_name.strip()} {last_name.strip()} - miło Cię poznać")


def identificator():
    id = random.randint(1, 99999)
    print(str(id).zfill(5))


def colours_searcher():
    colours = input("Podaj ulubione kolory rozdzielając przecinkiem: ")
    if colours.lower().find("niebieski") != -1:
        print("Jest niebieski")
    else:
        print("Nie ma niebieskiego")


if __name__ == '__main__':
    # run()
    # identificator()
    colours_searcher()

