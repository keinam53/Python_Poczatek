def run():
    path_to_file = "plain_text.txt"

    try:
        plain_text_file = open(path_to_file, mode="r")
        try:
            print("Wczytanie tekstu")
            text_data = plain_text_file.read()
        finally:
            print("Zamknięcie pliku")
            plain_text_file.close()
    except IOError:
        print("Nie udało się wczytać danych")
    else:
        print("Dane z pliku: ")
        print(text_data)


if __name__ == '__main__':
    run()