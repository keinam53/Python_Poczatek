import random
from student import Student


class School:

    MAX_STUDENTS_NUMBER = 20

    def __init__(self, name, students):
        self.name = name
        self.students = students
        self._promote_lucky_students()

    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def __str__(self):
        students = ""
        for student in self.students:
            students = students + "\n"
            students = students + str(student)
        return f"Szkoła: {self.name} z {len(self.students)} uczniami\nUczniowie:{students}"

    def assign_student(self, student):
        if len(self.students) < self.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            print("Nie ma więcej miejsc")

    @classmethod
    def create_schoow_witch_students(cls, school_name):
        numbber_of_students = random.randint(1, cls.MAX_STUDENTS_NUMBER)
        students = []
        for student_number in range(numbber_of_students):
            first_name = f"Student - {student_number}"
            last_name = f"Kowalski"
            students.append(Student(first_name, last_name))

        school = School(school_name, students)
        return school








