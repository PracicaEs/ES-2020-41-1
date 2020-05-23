class Hotel:

    def __init__(self, codi: str, nom: str, ciutat: str, num_pers: int, num_hab: int, dies_reserva: int, preu: float):
        self.codi = codi
        self.nom = nom
        self.ciutat = ciutat
        self.num_pers = num_pers
        self.num_hab = num_hab
        self.dies_reserva = dies_reserva
        self.preu_total = preu
        self.preu_persona = preu/num_pers
