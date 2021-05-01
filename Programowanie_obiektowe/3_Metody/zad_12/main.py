from shop.Order import generate_order
from shop.Apple import Apple
from shop.Potato import Potato


def run():
    gala = Apple(species_name="Gala", size="S", price=3.2)
    gloster = Apple(species_name="Gloster", size="M", price=4)
    bryza = Potato(species_name="Bryza", size="L", price=2.3)
    etiuda = Potato(species_name="Etiuda", size="M", price=2.9)
    print(f"4 kd jabłek Gala kosztuje {gala.calculate_price(4)} PLN")
    print(f"6 kd jabłek Gloster kosztuje {gloster.calculate_price(6)} PLN")
    print(f"10 kd ziemniaków Bryza kosztuje {bryza.calculate_price(10)} PLN")
    print(f"8 kd ziemniaków Etiuda kosztuje {etiuda.calculate_price(8)} PLN")
    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()


if __name__ == "__main__":
    run()