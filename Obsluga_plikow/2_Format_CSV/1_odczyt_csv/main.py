from estudent.persistence import load_from_csv


def run():
    for student in load_from_csv():
        print(student)


if __name__ == '__main__':
    run()
