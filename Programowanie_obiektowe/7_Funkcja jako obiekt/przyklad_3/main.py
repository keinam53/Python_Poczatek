from estudent.school import School
from estudent.grade_calculator import GradeCalculator


def run_example():
    school = School.create_school_with_students("Moja szkoła")
    students = school.students
    for student in students:
        print(student)
    print("-" * 20)

    # for student in students:
    #     student.add_final_grade(1, check_promotion_policy=GradeCalculator.normal_promotion_policy)
    # for student in students:
    #     print(student)
    # print("-" * 20)
    #
    students.sort(key=lambda student: student.grades_avg(), reverse=True)
    for student in students:
        print(student)


if __name__ == '__main__':
    run_example()
