from estudent.persistence import load_from_csv, save_as_csv
from estudent import data_generator


def run():
    students = data_generator.generate_students(number_of_students=10)
    save_as_csv(students)


if __name__ == '__main__':
    run()
