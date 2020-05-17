from src.User import *
from src.PaymentData import *


class Bank:

    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        print("Pago realizado con éxito")
        return True
