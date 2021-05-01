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
    def __init__(self, name, subject, depatrment):
        super().__init__(name, subject)
        self.guided_department = depatrment
        self.assigned_department = [depatrment]

    def send_message_from_parents(self, message):
        print(f"Wiadomość od rodziców wysłana: '{message}'")

    def __str__(self):
        return f"Nauczyciel: {self.name} | Przedmiot: {self.subject} | Wychowawca: {self.guided_department} |" \
               f"Uczy klasy: {self.assigned_department}"


def run():
    # nauczyciel = Teacher("Jan", "Biologia")
    # nauczyciel.assign_department("Ic IIa Vb")
    # print(nauczyciel)
    wychowawca = Tutor("Marcin", "Matematyka", "Va")
    wychowawca.assign_department("VIc")
    print(wychowawca)
    print(f"{wychowawca.name} - Wychowawca klasy: {wychowawca.guided_department}")
    wychowawca.send_message_from_parents("Pozdrowienia")


if __name__ == '__main__':
    run()
