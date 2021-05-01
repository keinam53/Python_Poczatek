def run():
    shopping_list = ["woda", "chleb", "mąka"]
    my_list = shopping_list
    your_list = shopping_list

    print("Lista zakupów:", shopping_list)
    print("Moja lista: ", my_list)
    print("Twoja lista: ", your_list)

    print(id(shopping_list))
    print(id(my_list))
    print(id(your_list))

    print("Dodaję ciastka do mojej listy")
    my_list.append("ciastka")

    print("Lista zakupów:", shopping_list)
    print("Moja lista: ", my_list)
    print("Twoja lista: ", your_list)

    print(id(shopping_list))
    print(id(my_list))
    print(id(your_list))

    hello_str = "Hello"
    my_str = hello_str
    your_str = hello_str

    print("Hello str: ", hello_str)
    print("my str: ", my_str)
    print("your_str: ", your_str)

    print(id(hello_str))
    print(id(my_str))
    print(id(your_str))

    print("Zmieniam przywitanie")
    my_str = "Hello World"

    print("Hello str: ", hello_str)
    print("my str: ", my_str)
    print("your_str: ", your_str)

    print(id(hello_str))
    print(id(my_str))
    print(id(your_str))

    dict = {"A": 1, "B": 2, "C": 3}
    my_dict = dict
    your_dict = dict

    print(dict)
    print(my_dict)
    print(your_dict)

    print(id(dict))
    print(id(my_dict))
    print(id(your_dict))

    my_dict.update(D=4)

    print(dict)
    print(my_dict)
    print(your_dict)

    print(id(dict))
    print(id(my_dict))
    print(id(your_dict))


if __name__ == '__main__':
    run()