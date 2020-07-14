class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return f"%.{self.places}f" % self.number


class Currency(Decimal):
    def __init__(self, symbol, number, places):
        super().__init__(number, places)
        self.symbol = symbol

    def __repr__(self):
        return f"{self.symbol}{super().__repr__()}"


print(Decimal(15.6789, 3))
print(Currency('$', 15.6789, 3))