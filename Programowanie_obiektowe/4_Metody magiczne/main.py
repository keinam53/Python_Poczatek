from shop.Order import generate_order
from shop.Apple import Apple
from shop.Potato import Potato
from shop.Product import Product
from shop.order_element import OrderElement
from shop.Order import Order

def run_homework():
    # first_order = generate_order()
    # print(first_order)
    # print(f"Liczba pozycji w zamówieniu: {len(first_order)}")
    # second_order = generate_order()
    # print(second_order)
    # print(f"Liczba pozycji w zamówieniu: {len(second_order)}")
    # gala = Apple(species_name="Gala", size="S", price=3.2)
    # gloster = Apple(species_name="Gloster", size="M", price=4)
    # bryza = Potato(species_name="Bryza", size="L", price=2.3)
    # etiuda = Potato(species_name="Etiuda", size="M", price=2.9)
    # print(gala)
    # print(gloster)
    # print(bryza)
    # print(etiuda)
    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    juice = Product("Sok", "Napoje", 6)
    first_order_elements = [
        OrderElement(product=cookie, quantity=3),
        OrderElement(product=juice, quantity=4)
    ]
    second_order_elements = [
        OrderElement(product=juice, quantity=4),
        OrderElement(product=cookie, quantity=3)
    ]
    first_order_eq = Order("Mariusz", "Baran", first_order_elements)
    second_order_eq = Order("Mariusz", "Baran", second_order_elements)

    if first_order_eq == second_order_eq:
        print("Zamówienia są takie same")
    else:
        print("Zamówienia są różne")


if __name__ == '__main__':
    run_homework()