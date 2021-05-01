from school import School
from student import Student

def run():
    school = School.create_schoow_witch_students("nr. 3")
    print(f"W szkole może być maksymalnie {school.MAX_STUDENTS_NUMBER} uczniów\n")
    # new_school = School.create_schoow_witch_students("Nowa szkoła")
    # print(new_school)
    # print(f"W nowej szkole może być maksymalnie {new_school.MAX_STUDENTS_NUMBER} uczniów")
    marcin = Student("Marcin", "Borchowiec")
    school.assign_student(marcin)
    print(school)

if __name__ == '__main__':
    run()