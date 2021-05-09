def run():
    with open("plain_text.txt", mode="r") as plain_text_file:
        print(plain_text_file.read(10))
        print(plain_text_file.read(10))


if __name__ == '__main__':
    run()