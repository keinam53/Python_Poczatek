from estudent.errors import LogicError, PlacesLimitError
from estudent.student import Student
from estudent.school import School
from estudent.data_generator import generate_students


def run():
    # student = Student("Mariusz", "Baran")
    # try:
    #     print(student.grades_avg)
    # except LogicError as error:
    #     print(f"{error}")

    students = generate_students(250)
    school = School("Szkoła", [])
    try:
        school.students = students
    except PlacesLimitError as error:
        print(f"{error}")


if __name__ == '__main__':
    run()
