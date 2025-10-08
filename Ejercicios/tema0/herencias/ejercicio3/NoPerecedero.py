from Ejercicios.tema0.herencias.ejercicio3.Producto import *

class NoPerecedero(Producto):
    
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo=tipo
    
    