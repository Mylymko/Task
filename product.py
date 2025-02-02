import logging

logger = logging.getLogger(__name__)

class InvalidPriceError(Exception):

    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def set_price(self, price):
        if price <= 0:
            logger.error(f"Недійсна ціна для товару {self.name}: {price} грн")
            raise InvalidPriceError("Ціна товару повинна бути більше нуля.")
        self.price = price
        logger.info(f"Ціна товару {self.name} встановлена: {self.price} грн")

if __name__ == "main":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s • %(levelname)s • %(message)s')

    try:
        product1 = Product("Товар 1", 100)
        product2 = Product("Товар 2", -50)
    except InvalidPriceError as e:
        print(f"Помилка: {e}")