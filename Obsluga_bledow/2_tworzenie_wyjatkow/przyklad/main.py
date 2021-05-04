from estudent import data_generator
from estudent.school import School
from estudent.grade_calculator import GradeCalculator


def run():
    students = data_generator.generate_students(number_of_students=250)
    school = School(name="Mała szkoła", students=[])
    school.students = students
    print(school)

    # student_avg = GradeCalculator.calculate_student_avg([])


if __name__ == '__main__':
    run()