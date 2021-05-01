# class Student:
#     pass
#
#
# class Grade:
#     pass
#
#
# class School:
#     pass
#
#
# if __name__ == "__main__":
#     student_mariusz = Student()
#
#     grade_a = Grade()
#     grade_f = Grade()
#
#     my_school = School()
#
#     # print(student_mariusz)
#     # print(grade_a, grade_f)
#     # print(my_school)
#
# all_students = [Student(), Student(), Student(), Student(), Student()]
# print(all_students)
# print(all_students[0])
#
# grades = {
#     1: Grade(),
#     2: Grade(),
#     3: Grade(),
#     4: Grade(),
#     5: Grade(),
#     6: Grade()
# }
# print(grades)

#ZAD 1

class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


gala = Apple()
gloster = Apple()
goldstar = Apple()
bryza = Potato()
etiuda = Potato()
malaga = Potato()
print(type(gala))
print(type(gloster))
print(type(goldstar))
print(type(bryza))
print(type(etiuda))
print(type(malaga))
orders = [Order(), Order(), Order(), Order(), Order()]
print(orders)
products = {
    "chleb": Product(),
    "bułki": Product(),
    "masło": Product(),
    "ser": Product()
}
print(products)