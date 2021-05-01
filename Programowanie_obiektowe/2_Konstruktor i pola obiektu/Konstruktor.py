# class Student:
#     def __init__(self):
#         print("Tworzy się obiekt")
#
#
# if __name__ == "__main__":
#     student = Student()

class Student:
    def __init__(self):
        self.first_name = "Mariusz"
        self.last_name = "Baran"
        self.age = 25
def run_example():
    student = Student()
    print(student)
    print(student.first_name)
    print(student.last_name)
    print(student.age)
# stan można modyfikować
    student.first_name = "Marcin"
    student.last_name = "Borchowiec"
    student.age = 32
    print(student.first_name)
    print(student.last_name)
    print(student.age)
if __name__ == "__main__":
    run_example()
