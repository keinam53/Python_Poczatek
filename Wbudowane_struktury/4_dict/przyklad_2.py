# dict comprehensions
import random


def run():
    expenditures_names = ["prąd", "woda", "zakupy"]
    expenditures = {expenditure_name: random.randint(1, 100) for expenditure_name in expenditures_names}
    print(expenditures)

    # można korzystać z if
    student_names = ["Damian", "Mariusz", "Adam", "Konstanty"]
    students = {student_name: random.randint(1, 999) for student_name in student_names}
    print(students)

    new_students = {f"{name[:1]}...": number * 10 for name, number in students.items()}
    print(new_students)


if __name__ == '__main__':
    run()