from szkola.school import create_school_with_students


def run():
    school = create_school_with_students("Nr. 3")
    school.print_self()


if __name__ == "__main__":
    run()
