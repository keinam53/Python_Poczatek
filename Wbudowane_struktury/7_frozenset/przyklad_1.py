def run():
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy", "Kawowy"]
    my_favourite_flavours = frozenset(flavours)
    print(my_favourite_flavours)

    # your_favourite_flavours = frozenset({"Orzechowy", "Pistacjowy", "Kawowy"})
    # print(your_favourite_flavours)

    # frozenset usuwa duplikaty, można wykorzystywać metody matematyczne
    your_favourite_flavours = frozenset({"Orzechowy", "Pistacjowy", "Kawowy", "Kawowy", "Kawowy"})
    print(your_favourite_flavours)
    common_flavours = my_favourite_flavours.intersection(your_favourite_flavours)
    print(common_flavours)
    all_flavours = my_favourite_flavours.union(your_favourite_flavours)
    print(all_flavours)

    # Nie pozwala na modyfikacje

    # frozenset jest immutable - można twarzyć zbiór zbiorów
    set_of_set = {frozenset({"karmel", "mango"}), frozenset({"czekolada", "wiśnia"})}
    print(set_of_set)

    
if __name__ == "__main__":
    run()