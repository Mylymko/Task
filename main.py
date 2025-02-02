import logging
from product import Product, InvalidPriceError
from payment import CreditCardProcessor
from discount import PercentageDiscount
from cart import Cart

logging.basicConfig(level=logging.INFO, format='%(asctime)s • %(levelname)s • %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    cart1 = None

    try:
        product1 = Product("Товар 1", 100)
        product2 = Product("Товар 2", 200)

        cart1 = Cart()
        cart1.add_product(product1)
        cart1.add_product(product2)

        cart2 = Cart()
        cart2.add_product(Product("Товар 3", 150))
        cart2.add_product(Product("Товар 4", 250))

        cart1 += cart2

        percentage_discount = PercentageDiscount(10)

        total_with_discount = cart1.total() * (1 - percentage_discount.percentage / 100)
        print(f"Загальна вартість з дисконтом: {total_with_discount} грн")

        credit_card_processor = CreditCardProcessor()
        cart1.pay(credit_card_processor)

    except InvalidPriceError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    if cart1 is not None:
        print(cart1)
        print(f"Загальна вартість: {cart1.total()} грн")
    else:
        print("Кошик cart1 не було створено.")