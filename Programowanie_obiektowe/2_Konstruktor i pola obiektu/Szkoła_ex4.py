import random


class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        promote_lucky_student(students)


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promotion = False


def promote_lucky_student(students):
    for index, student in enumerate(students):
        if index %3 == 0:
            promote_student(student)


def promote_student(student):
    student.promotion = True


def print_student(student):
     print(f"Student: {student.first_name} {student.last_name}, Promocja: {student.promotion}")


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for studnet_number in range(number_of_students):
        first_name = f"Student {studnet_number}"
        last_name = "Nowak"
        students.append(Student(first_name, last_name))
    school = School(school_name, students)
    return school


def run_example():
    school = create_school_with_students("nr. 3 w Lubnie")
    print(school)
    for student in school.students:
        print_student(student)


if __name__ == "__main__":
    run_example()
