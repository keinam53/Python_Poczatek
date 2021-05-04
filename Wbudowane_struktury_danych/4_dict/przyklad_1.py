def run():
    expenditures = {
        "prąd": [300],
        "woda": [30.45],
        "zakupy": [120.15, 170.53, 20.15]
    }
    print(expenditures)

    # clear usuwa
    # expenditures.clear()
    # print(expenditures)

    # copy - zwraca kopię
    copy_expenditures = expenditures.copy()
    print(copy_expenditures)

    # get - wyświetla wartość po kluczu
    water_cost = expenditures.get("woda")
    print(water_cost)
    cookies_cost = expenditures.get("ciastka", [10])
    print(cookies_cost)

    # update = aktualizuje słownik
    expenditures.update(jedzenie=[120], rozrywka=[70])
    print(expenditures)

    other_expenditures = {"remont": [1400], "internet": [80]}
    expenditures.update(other_expenditures)
    print(expenditures)


if __name__ == '__main__':
    run()