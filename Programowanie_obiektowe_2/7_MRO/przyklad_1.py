class Grandparent:

    def say_hello(self):
        print("Hello Grandpa")


class ParentOne(Grandparent):
    def say_hello(self):
        print("Hello Parent One")


class ParentTwo(Grandparent):
    def say_hello(self):
        print("Hello Parent Two")


class Child (ParentOne, ParentTwo):
    def say_hello(self):
        print("Hello Child")


def run():
    # child = Child()
    # child.say_hello()
    print(Child.mro())


if __name__ == "__main__":
    run()