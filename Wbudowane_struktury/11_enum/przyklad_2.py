from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        # return count
        return name


class Color(AutoName):
    NIEBIESKI = auto()
    ZIELONY = auto()
    CZERWONY = auto()


# class Color(Enum):
#     NIEBIESKI = auto()
#     ZIELONY = auto()
#     CZERWONY = auto()


def run():
    niebieski = Color.NIEBIESKI
    zielony = Color.ZIELONY
    print(niebieski.name, niebieski.value)
    print(zielony.name, zielony.value)





if __name__ == '__main__':
    run()
