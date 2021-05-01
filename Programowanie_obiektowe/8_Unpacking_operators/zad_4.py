def wypisz_str(**kwargs):
    napis = ""
    for argument_name, argument_value in kwargs.items():
        napis += f"{argument_name} = {argument_value}, "
    print(napis)

def run():
    eng_pl = {
        "storm": "burza",
        "car": "samochód",
        "bike": "rower"
    }

    pl_eng = {
        "pieniądze": "money",
        "kawa": "coffee",
        "słuchawki": "headphones"
    }
    slownik = {**eng_pl, **pl_eng}
    print(slownik)

    wypisz_str(**slownik)


if __name__ =='__main__':
    run()