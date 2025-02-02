import logging

logger = logging.getLogger(__name__)


class Discount:
    def apply(self, price):
        raise NotImplementedError("Цей метод має бути перевизначений у підкласах.")


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        if not isinstance(percentage, (int, float)):
            raise ValueError("Відсоток має бути числом.")

        self.percentage = percentage
        logger.info(f"Знижка встановлена: {self.percentage}%")

    def apply(self, price):
        discounted_price = price * (1 - self.percentage / 100)
        logger.info(f"Застосовано {self.percentage}% знижку: нова ціна {discounted_price} грн")
        return discounted_price