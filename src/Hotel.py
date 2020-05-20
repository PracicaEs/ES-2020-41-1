class Hotel:

    def __init__(self, codi: str, nom: str, num_pers: int, num_hab: int, dies_reserva: int):
        self.codi = codi
        self.nom = nom
        self.num_pers = num_pers
        self.num_hab = num_hab
        self.dies_reserva = dies_reserva

    def get_codi(self) -> str:
        return self.codi

    def get_nom(self) -> str:
        return self.nom

    def get_num_pers(self) -> int:
        return self.num_pers

    def get_num_hab(self) -> int:
        return self.num_hab

    def get_dies_reserva(self) -> int:
        return self.dies_reserva
