from shop.apple import Apple
from shop.potato import Potato


def run():
    gala = Apple("Gala", "M", 2.8)
    print(gala)
    bryza = Potato("Bryza", "S", 1.9)
    print(bryza)


if __name__ == '__main__':
    run()

