from estudent import data_generator
from estudent.school import School


def run_example():
    students = data_generator.generate_students()
    school = School(name="Hogwart", students=students)
    best_student = school.best_student
    print(school)

    print(f"Średnia najlepszego ucznia: {best_student.grades_avg}")
    print(f"Oceny najlepszego ucznia: {best_student.final_grades}")


if __name__ == '__main__':
    run_example()