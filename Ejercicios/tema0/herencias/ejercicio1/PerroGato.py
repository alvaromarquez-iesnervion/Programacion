from Animal import *

class Perro(Animal):
    def __init__(self, nombre, nPatas):
        super().__init__(nombre, nPatas)

    def habla(self):
        return "Guau"
    
    def __str__(self):
        return "Soy un perro. " + super().__str__()



class Gato(Animal):
    def __init__(self, nombre, nPatas):
        super().__init__(nombre, nPatas)

    def habla(self):
        return "Miau"
    
    def __str__(self):
        return "Soy un gato. " + super().__str__()

    
