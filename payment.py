import logging

logger = logging.getLogger(__name__)

class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError("Цей метод має бути перевизначений у підкласах.")

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        logger.info(f"Оплата кредитною карткою: {amount} грн")
        print(f"Оплата кредитною карткою: {amount} грн")

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount):
        logger.info(f"Оплата через PayPal: {amount} грн")
        print(f"Оплата через PayPal: {amount} грн")

class BankTransferProcessor(PaymentProcessor):
    def pay(self, amount):
        logger.info(f"Банківський переказ: {amount} грн")
        print(f"Банківський переказ: {amount} грн")