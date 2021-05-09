import os


def process_text_file(file_path):
    with open(file_path, mode="r") as plain_text_file:
        plain_data = plain_text_file.read()

    print("Dane z pliku:")
    print(plain_data)


def run():
    absolute_path = "C:\\Users\\Mariusz Baran\\PycharmProjects\Obsluga_plikow" \
                    "\\1_Praca_z_plikami\\4_sciezka_absolutna\\plain_text.txt"
    absolute_path = os.path.normpath(absolute_path)
    try:
        process_text_file(absolute_path)
    except IOError:
        print("Nie można wczyatć danych z pliku")


if __name__ == '__main__':
    run()