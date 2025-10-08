
class Producto():
    
    def __init__(self, nombre, precio):

        self.nombre=nombre
        self.precio=precio

    def calcular(self, cantidad):
        result= cantidad * self.precio

        return result
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}€"

    def __lt__(self, other):
        if isinstance(other, Producto):
            return self.precio < other.precio
        return NotImplemented

