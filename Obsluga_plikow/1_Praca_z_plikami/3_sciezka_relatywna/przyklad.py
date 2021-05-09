import os


def process_text_file(file_path):
    with open(file_path, mode="r") as plain_text_file:
        plain_data = plain_text_file.read()

    print("Dane z pliku:")
    print(plain_data)


def run():
    path_in_dir = os.path.join("folder", "other_file.txt")
    try:
        process_text_file(path_in_dir)
    except IOError:
        print("Nie można wczyatć danych z pliku")


if __name__ == '__main__':
    run()