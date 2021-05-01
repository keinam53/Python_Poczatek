from Order import Order


class ExpressOrder(Order):
    def __init__(self, client_first_name, client_last_name, delivery_date, order_elements=None):
        super().__init__(client_first_name, client_last_name)
        self.delivery_date = delivery_date
        self.EXTRA_PRICE = 20

        if order_elements is None:
            order_elements = []

        self.order_elements = order_elements
        self.cena_bez_oplaty = self.total_price - self.EXTRA_PRICE

    @property
    def total_price(self):
        return super().total_price + self.EXTRA_PRICE

    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Ekspresowe zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price:.2f} PLN"
        product_details = "Zamówione produkty:\n"
        oplata_dodatkowa = f"Opłata dodatkowa wynosi: {self.EXTRA_PRICE} PLN"
        termin_dostawy = f"Termin dostawy do: {self.delivery_date}"
        cena_bez_opl = f"Cena bez opłaty wynosi: {self.cena_bez_oplaty}"
        for element in self._order_elements:
            product_details = product_details + "\t" + f"{element}" + "\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, cena_bez_opl, oplata_dodatkowa, termin_dostawy])
        return result