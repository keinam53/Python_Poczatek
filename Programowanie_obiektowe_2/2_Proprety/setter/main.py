from estudent import data_generator
from estudent.school import School


def run():
    students = data_generator.generate_students()
    school = School("Moja szkoła", students)
    # print(school)
    #
    # new_students = data_generator.generate_students(8)
    # school.students = new_students
    # print(school)

    too_many_students = data_generator.generate_students(100)
    school.students = too_many_students
    print(school)

if __name__ == '__main__':
    run()