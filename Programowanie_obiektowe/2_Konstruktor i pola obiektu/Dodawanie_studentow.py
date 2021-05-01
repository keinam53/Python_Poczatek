class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promotion = False


def print_student(student):
    print(f"Imię: {student.first_name} {student.last_name}, Promocja: {student.promotion}")


def promote_student(student):
    student.promotion = True


def run_example():
    ola = Student(first_name="Ola", last_name="Bąk")
    print_student(ola)

    jan = Student("Jan", "Kowal")
    print_student(jan)

    promote_student(ola)
    print_student(ola)


if __name__ == "__main__":
    run_example()





