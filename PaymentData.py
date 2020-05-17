class PaymentData:

    def __init__(self):
        self.tipo_tarjeta = ""
        self.nom_titular = ""
        self.codigo_seg = None
        self.importe = None

    def get_payment_data(self):
        return self.importe
