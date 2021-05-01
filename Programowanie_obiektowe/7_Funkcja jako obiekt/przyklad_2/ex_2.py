import random


def say_hello():
    print("Hello")

 
def say_goodbye():
    print("Goodbye")


def randomize_func(first, second):
    number = random.randint(1, 2)
    if number == 1:
        return first
    else:
        return second


def run():
    hello_or_goodbye = randomize_func(say_hello, say_goodbye)
    hello_or_goodbye()


if __name__ == '__main__':
    run()