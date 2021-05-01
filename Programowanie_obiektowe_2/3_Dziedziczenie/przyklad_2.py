class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_department = []

    def assign_department(self, department):
        self.assigned_department.append(department)

    def __str__(self):
        return f"Nauczyciel: {self.name} | Przedmiot: {self.subject} | Klasy: {self.assigned_department}"


class Tutor(Teacher):
    def __init__(self, name, subject, department):
        super().__init__(name, subject)
        self.guided_department = department

    def message_from_parents(self, message):
        print(f"Wiadomość od rodziców: {message}")


def run():
    tutor = Tutor("Jan", "WF", "Ib")
    tutor.assign_department("Vc, IIIa")
    print(tutor.assigned_department)
    print(tutor.guided_department)
    print(tutor)


if __name__ == '__main__':
    run()
