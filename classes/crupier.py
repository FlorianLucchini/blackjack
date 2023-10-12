from jugador import Jugador

class Crupier(Jugador): 
    def __init__(self, id: int, nombre: str) -> None:
        super().__init__(id, nombre)
        self.apostadores : dict = {}
    
    def getApostadores(self):
        "Mostrará los apostadores que jugarán con este crupier."
        return self.apostadores.keys()
        
    def getApostadorPorNombre(self, nombre):
        return self.apostadores.get(nombre, "No ")