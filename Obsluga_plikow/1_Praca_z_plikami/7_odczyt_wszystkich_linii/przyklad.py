def run():
    with open("plain_text.txt", mode="r") as plain_text_file:
        # lines = plain_text_file.readlines()
        for line_number, line in enumerate(plain_text_file):
            print(f"{line_number}) {line}")


if __name__ == '__main__':
    run()