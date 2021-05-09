import csv

from student import Student


def load_from_csv(file_name="students.csv"):
    with open(file_name, newline="") as students_file:
        csv_reader = csv.reader(students_file)
        students = []
        for row_index, row in enumerate(csv_reader):
            if row_index == 0:
                continue
            grades_values = [int(value) for value in row[3].split(",")]

            students.append(
                Student.from_csv(
                    first_name=row[0],
                    last_name=row[1],
                    promoted=str_to_bool(row[2]),
                    grades_value=grades_values
                )
            )
    return students


def str_to_bool(str_bool):
    if str_bool == "True":
        return True
    elif str_bool == "False":
        return False
    raise ValueError("Nieprawidłowa wartość dla typu bool")
