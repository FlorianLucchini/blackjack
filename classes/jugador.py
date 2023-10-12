class Jugador:
    def __init__(self, id : int, nombre : str) -> None:
        self.id = id
        self.nombre = nombre
        self.monto : int = (self.ganancia - self.perdida)
        self.ganancia = 0
        self.perdida = 0
        
    def getMonto(self):
        return self.monto
    
    def getGanacia(self):
        return self.ganancia
    
    def getPerdida(self):
        return self.perdida
    
    def actualizarGanancia(self, apuesta : int):
        (self.ganancia + apuesta)
        
    def actualizarPerdida(self, apuesta : int):
        (self.perdida + apuesta)