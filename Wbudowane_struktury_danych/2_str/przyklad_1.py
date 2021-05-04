def run():
    number_parts = ["123", "456", "789", "345"]
    print("-".join(number_parts))
    print("".join(number_parts))

    name = "-|  Mariusz  |-"
    left_clean = name.lstrip("-| ")
    right_clran = name.rstrip("-| ")
    both_clean = name.strip("-| ")
    print(name)
    print(f"{left_clean} B")
    print(f"{right_clran} B")
    print(f"{both_clean} B")

    # startswith i endswith sprawdzają czy napis zaczyna i kończy się wyrażeniem
    first_name = "Mariusz"
    print(first_name.startswith("Mar"))
    print(first_name.startswith("Rob"))
    print(first_name.endswith("sz"))
    print(first_name.endswith("in"))

    # zfill dopełnia zarami z przodu
    number_id = 123
    id = str(number_id).zfill(8)
    print(id)

    # find oraz index szukają wyrażenia w napisie
    napis = "Ale dzisiaj ładny dzień, wczoraj też był dzień"
    print(napis.find("dzień", 20))
    print(napis.index("dzień"))


if __name__ == '__main__':
    run()