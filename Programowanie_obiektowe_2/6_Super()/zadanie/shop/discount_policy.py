class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_price):
        discount = total_price * (self.percentage * 0.01)
        return total_price - discount


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, total_discount):
        self.total_discount = total_discount

    def apply_discount(self, total_price):
        if self.total_discount < total_price:
            return total_price - self.total_discount
        else:
            return 0


