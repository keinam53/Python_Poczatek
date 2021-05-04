products = {
    "chleb": {
        "quantity": 100,
        "priece": 3.5
    },
    "jabłka": {
        "quantity": 200,
        "priece": 3.1
    }
}


def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity
