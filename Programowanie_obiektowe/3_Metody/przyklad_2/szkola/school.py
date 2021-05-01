import random
from szkola.student import Student


class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students
        self.promote_lucky_student()

    def promote_lucky_student(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def print_self(self):
        print(f"Szkoła: {self.name} z {len(self.students)} studentami")
        for student in self.students:
            student.print_self()


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student - {student_number + 1} "
        last_name = "Nowak"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school
