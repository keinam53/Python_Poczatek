from shop.products_store import products
from shop.products_store import update_product_quantity

orders = []


def create_new_order(product_name, quantity):
    priece = products[product_name]["priece"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("Nie mamy tyle towaru")
        return None
    total_price = priece * quantity
    new_order = {
        "Produkt": product_name,
        "Ilość": quantity,
        "Cena": total_price
    }
    update_product_quantity(product_name, quantity)
    return new_order
