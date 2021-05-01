import random


class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price


class Order:
    def __init__(self, client_first_name, client_last_name, products=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if products is None:
            products = []
        self.products = products
        total_price = 0
        for product in products:
            total_price = total_price + product.unit_price
        self.total_price = total_price


class Apple:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


def print_product(product):
    print(f"Produkt: {product.name}, Kategoria: {product.category_name}, Cena: {product.unit_price} ")


def print_order(order):
    print("=" * 20)
    print(f"Zamówienie złożone przez {order.client_first_name} {order.client_last_name}")
    print(f"Wartość zamówienia: {order.total_price} PLN")
    print("Zamówione produkty:")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("=" * 20)
    print()


def generate_order():
    number_of_products = random.randint(1, 20)
    products = []
    for product_number in range(number_of_products):
        product_name = f"Produkt - {product_number + 1}"
        category = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category, unit_price)
        products.append(product)

    order = Order("Mariusz", "Baran", products)
    return order


def run():
    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)

# ZAD 2
# def run():
#     gala = Apple(species_name="gala", size="M", price=3.5)
#     gloster = Apple(species_name="gloster", size="S", price=4)
#     goldstar = Apple(species_name="goldstar", size="L", price=4.7)
#
#
#     bryza = Potato(species_name="bryza", size="M", price=2)
#     etiuda = Potato(species_name="etiuda", size="L", price=2.3)
#     malaga = Potato(species_name="malaga", size="L", price=2.9)
#
#     cheese = Product(name="Cheese", category_name="Food", unit_price=6)
#     rice = Product(name="Ryż", category_name="Food", unit_price=3.4)
#     soap = Product(name="Mydło", category_name="Chemistry", unit_price=5)
#     empty_order = Order(client_first_name="Mariusz", client_last_name="Baran")
#     order = Order(client_first_name="Mariusz", client_last_name="Baran", products=[rice, cheese, soap])
#     # print_order(empty_order)
#     print_order(order)


if __name__ == "__main__":
    run()
