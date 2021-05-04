def find_best_grade(grades_by_subject):
    best_grade = 0
    for subject, grades in grades_by_subject.items():
        best_grade_by_subject = max(grades)
        if best_grade_by_subject > best_grade:
            best_grade = best_grade_by_subject
    return best_grade
zbior_ocen = {
    "Matematyka": [5, 2, 3, 1, 4],
    "Fizyka": [2, 4, 3, 1, 5, 2],
    "Biologia" : [4, 5, 6, 2, 3]
}
najlepsza_ocena = find_best_grade(zbior_ocen)
print(f"Najlepsza ocena: {najlepsza_ocena}")
