class TaxRates:

    OWOCE_I_WARZYWA = 0.05
    JEDZENIE = 0.08
    INNE = 0.2

class TaxCalculator:

    @staticmethod
    def tax_for_order_element(order_element):
        product_cathegory = order_element.product.category_name
        if product_cathegory == "Owoce i warzywa":
            tax_rate = TaxRates.OWOCE_I_WARZYWA
        elif product_cathegory == "Jedzenie":
            tax_rate = TaxRates.JEDZENIE
        else:
            tax_rate = TaxRates.INNE
        return tax_rate * order_element.calculate_price()
