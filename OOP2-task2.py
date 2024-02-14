from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, currency, value):
        self.currency = currency
        self.value = value

    def get_value(self):
        return self.value

    def get_currency(self):
        return self.currency

    @abstractmethod
    def convert_to_currency(self, target_currency, conversion_rate):
        pass


class Cash(Money):
    def __init__(self, currency, value, denomination):
        super().__init__(currency, value)
        self.denomination = denomination

    def convert_to_currency(self, target_currency, conversion_rate):
        if self.currency == target_currency:
            return self.value
        else:
            converted_value = self.value * conversion_rate
            return converted_value


class Card(Money):
    def __init__(self, currency, value, credit_limit):
        super().__init__(currency, value)
        self.credit_limit = credit_limit

    def convert_to_currency(self, target_currency, conversion_rate):
        if self.currency == target_currency:
            return self.value
        else:
            converted_value = self.value * conversion_rate
            return converted_value


# Example usage
cash = Cash("USD", 100, "20 dollar bills")
card = Card("EUR", 500, 1000)

conversion_rate = 0.82  # Example conversion rate from USD to EUR

print("Cash value in USD:", cash.get_value())
print("Cash value in EUR:", cash.convert_to_currency("EUR", conversion_rate))

print("Card value in EUR:", card.get_value())
print("Card value in USD:", card.convert_to_currency("USD", 1 / conversion_rate))
