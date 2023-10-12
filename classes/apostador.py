from jugador import Jugador

class Apostador(Jugador):
    def __init__(self, id : int, nombre: str) -> None:
        super().__init__(id, nombre)