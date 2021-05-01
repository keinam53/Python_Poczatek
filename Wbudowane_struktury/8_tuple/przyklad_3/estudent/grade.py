class Grade:

    FAILING_GRADE = 1

    def __init__(self, value):
        self.value = value

    def is_passing(self):
        return self.value > Grade.FAILING_GRADE

    def __repr__(self):
        return str(self.value)


class FinalGrade(Grade):

    def __init__(self, value, subject):
        super().__init__(value)
        self.subject = subject

    def __repr__(self):
        return f"{self.subject}: {self.value}"