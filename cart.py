import logging
from product import Product

logger = logging.getLogger(__name__)

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total(self):
        return sum(product.price for product in self.items)

    def pay(self, payment_processor):
        total_amount = self.total()
        payment_processor.pay(total_amount)

    def __iadd__(self, other):
        if not isinstance(other, Cart):
            raise TypeError("Можна додавати лише інші кошики.")
        self.items.extend(other.items)
        return self

    def __str__(self):
        return f"Кошик з товарами: {', '.join([product.name for product in self.items])}"

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.items):
            product = self.items[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration