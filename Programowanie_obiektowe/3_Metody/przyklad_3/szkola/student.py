class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.final_grade = []

    def promote(self):
        self.promoted = True

    def print_self(self):
        print(f"Studnet: {self.first_name} {self.last_name} | Promocja: {self.promoted} | Ocena: {self.final_grade}")

    def add_final_grade(self, grade):
        self.final_grade.append(grade)
        if grade == 1:
            self.promoted = False



