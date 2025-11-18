# Encapsulate using polymosphism
from typing import List

class PaymentBase:
    def __init__(self, amount: int):
        self.amount = amount

    def process_payment(self):
        pass

class CreditCard(PaymentBase):
    def process_payment(self) -> None:
        msg = f"Payment processing... CreditCard Payment: [{self.amount}]"
        print(msg)

class PayPal(PaymentBase):
    def process_payment(self) -> None:
        msg = f"Payment processing... Paypal Payment: [{self.amount}]"
        print(msg)

if __name__ == "__main__":
    payments: List[PaymentBase] = [CreditCard(200), PayPal(700)]
    for payment in payments:
        payment.process_payment()