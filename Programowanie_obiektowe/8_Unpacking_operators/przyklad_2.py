def print_grades(**kwargs):
    for subject, grade in kwargs.items():
        print(f"Przedmiot: {subject} Ocena: {grade}")

def run():
    print_grades(
        matematyka=4,
        fizyka=3,
        chemia=4,
        biologia=2,
        WF=5
    )

if __name__ == '__main__':
    run()