def print_grades(**kwargs):
    for subject, grade in kwargs.items():
        print(f"Przedmiot: {subject} Ocena: {grade}")

def run():
    grades = {
        "matematyka": 4,
        "fizyka": 3,
        "chemia": 4,

    }
    print_grades(**grades)

    more_grades = {
        "biologia": 2,
        "WF": 5,
        "technika": 5
    }
    all_grades = {**grades, **more_grades}
    print(all_grades)

if __name__ =='__main__':
    run()