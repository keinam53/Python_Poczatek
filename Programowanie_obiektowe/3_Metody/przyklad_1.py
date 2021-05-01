class Student:

    def __init__(self, name):
        self.name = name

    def print_something(self):
        print("Metoda klasy Student")

    def print_self(self):
        print(f"Czym jest self? {self}")
        print(f"Można wypisać imię: {self.name}")

    def do_all_work(self):
        print("Zaczynam pracę")
        self.do_piece_of_work()
        self.do_piece_of_work()
        self.do_piece_of_work()
        print("Koniec pracy")

    def do_piece_of_work(self):
        print("Robora...")


def run():
    student = Student("Mariusz")
    student.print_something()
    student.print_self()
    student.do_all_work()


if __name__ == "__main__":
    run()