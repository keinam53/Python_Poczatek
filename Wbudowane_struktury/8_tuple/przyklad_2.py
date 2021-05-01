def find_best_grade(subject_with_final_grades):
    best_subject = None
    best_final_grade = 0
    for subject, final_grade in subject_with_final_grades.items():
        if final_grade > best_final_grade:
            best_final_grade = final_grade
            best_subject = subject
    return best_subject, best_final_grade


def run_avg_speed(name, street, time):
    avg_speed = street / time
    return f"{name} biega z prędkością {avg_speed} km/h"


def run():
    subject_with_final_grades = {
        "Matematyka": 4,
        "Historia": 5,
        "Fizyka": 3,
        "Biologia": 4
    }
    best_subject, best_grade = find_best_grade(subject_with_final_grades)
    print(best_subject, best_grade)
    result = find_best_grade(subject_with_final_grades)
    print(result)

    seed = run_avg_speed("Mariusz", 20, 2)
    print(seed)


if __name__ == '__main__':
    run()