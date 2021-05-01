from school import promotion_status as status
from school.grade_calculator import calculate_student_final_grades
from school.promote import check_promotion
from school.students_data import is_student_in_school

print("Witaj w elektronicznym dzienniku!")

student_name = input("Podaj imię ucznia żeby dowiedzieć się czy zdał/zdała do następnej klasy: ")

if not is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma na liście...")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = check_promotion(final_grades)

    if promotion_result == status.PASSED:
        print(f"Gratuluję! {student_name} zdał/zdała do następnej klasy :)")
    elif promotion_result == status.FAILED:
        print(f"Niestety {student_name} nie zdał/nie zdała")
    else:
        print("Coś poszło nie tak... Zgłoś to obsłudze systemu")


