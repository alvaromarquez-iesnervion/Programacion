from Ejercicios.tema0.herencias.ejercicio3.Producto import *

class Perecedero(Producto):
    def __init__(self, nombre, precio, diasCaducar):
        super().__init__(nombre, precio)
        self.diasCaducar=diasCaducar
    
    def calcular(self, cantidad):
        precio= super().calcular(cantidad)
        if self.diasCaducar==1:
            precio = precio/4
        elif self.diasCaducar==2:
            precio=precio/3
        elif self.diasCaducar==3:
            precio=precio/2

        return precio