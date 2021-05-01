import random


def generate_list():
    lista = []
    for i in range(random.randint(5, 10)):
        lista.append(random.randint(1, 100))
    return lista


def run():
    lista_pierwsza = generate_list()
    lista_druga = generate_list()
    print(lista_pierwsza)
    print(lista_druga)

    polaczona_lista = [*lista_pierwsza, *lista_druga]
    print(polaczona_lista)


if __name__ == '__main__':
    run()