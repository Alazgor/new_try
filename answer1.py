class Currency:
    def __init__(self, code=None, amount=0, exchange_rate=1):
        self.code = code
        self.amount = amount
        self.exchange_rate = exchange_rate

    def set_code(self, code):
        self.code = code
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate
        return self

    def convert(self, new_code, new_exchange_rate):
        if self.code is None:
            raise ValueError("Currency code not set")
        self.amount *= self.exchange_rate / new_exchange_rate
        self.code = new_code
        self.exchange_rate = new_exchange_rate
        return self

    def __str__(self):
        return f"{self.code}: {self.amount}"


# Example Usage:
currency = Currency().set_code("USD").set_amount(100).set_exchange_rate(1.23)
print(currency)  # Output: USD: 100
currency.convert("EUR", 0.9)
print(currency)  # Output: EUR: 111.11111111111111
