from estudent.subject import Subject
from estudent.grade import Grade, FinalGrade


def run():
    best_grade = Grade(6)
    failing_grade = Grade(1)
    print(best_grade)
    print(failing_grade)
    print(best_grade.is_passing())
    print(failing_grade.is_passing())

    math = Subject(identifier=1, name="Matematyka", is_obligatory=True)
    # math = Subject(2, "WF", True)
    # print(math)

    # final_grade = FinalGrade(value=3, subject="WF")
    final_grade = FinalGrade(value=3, subject=math)
    print(final_grade)
    print(final_grade.is_passing())

    math.assign_teacher("Mariusz")
    math.assign_teacher("Adam")
    print(math)


if __name__ == '__main__':
    run()