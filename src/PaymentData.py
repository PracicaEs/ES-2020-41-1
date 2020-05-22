class PaymentData:

    def __init__(self, tipo_tarjeta, nom_titular, codigo_seg, importe):
        self.tipo_tarjeta = tipo_tarjeta
        self.nom_titular = nom_titular
        self.codigo_seg = codigo_seg
        self.importe = importe

    def confirm_data(self):
        correct = True
        if self.tipo_tarjeta != "VISA" and self.tipo_tarjeta != "MasterCard":
            correct = False
        elif self.codigo_seg < 0 or self.codigo_seg > 999:
            correct = False
        elif len(self.nom_titular) < 5:
            correct = False

        if correct:
            m_correct = "Datos correctos"
        else:
            m_correct = "Datos incorrectos"
        return m_correct
