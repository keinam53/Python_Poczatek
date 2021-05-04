from enum import Enum


class WeekStr():
    PONIEDZIALEK = "PONIEDZIALEK"
    WTOREK = "WTOREK"
    SRODA = "SRODA"
    CZWARTEK = "CZWARTEK"
    PIATEK = "PIATEK"
    SOBOTA = "SOBOTA"
    NIEDZIELA = "NIEDZIELA"


def is_weekend_str(day):
    return day == WeekStr.SOBOTA or day == WeekStr.NIEDZIELA


class Week(Enum):
    PONIEDZIALEK = 1
    WTOREK = 2
    SRODA = 3
    CZWARTEK = 4
    PIATEK = 5
    SOBOTA = 6
    NIEDZIELA = 7

    def is_weekend(self):
        return self.value > 5

    def is_earlier(self, other_day):
        return self.value < other_day.value


def run():
    wtorek = Week.WTOREK
    sobota = Week.SOBOTA
    # print(wtorek)
    # print(wtorek.name, wtorek.value)
    # print(wtorek is Week.WTOREK)
    # print(wtorek is Week.PIATEK)

    # print(is_weekend(wtorek))
    # print(is_weekend(7))
    # print(is_weekend_str(WeekStr.SOBOTA))
    # print(is_weekend_str("NIEDZIELA"))

    # day_of_week_number = int(input("Który dziś dzień tygodnia? "))
    # day_of_week = Week(day_of_week_number)
    # print(day_of_week)
    #
    # day_of_week_name = Week["PIATEK"]
    # print(day_of_week_name)
    # print(type(day_of_week_name))

    print(sobota.is_weekend())
    print(wtorek.is_weekend())
    print(wtorek.is_earlier(sobota))

    
if __name__ == '__main__':
    run()
