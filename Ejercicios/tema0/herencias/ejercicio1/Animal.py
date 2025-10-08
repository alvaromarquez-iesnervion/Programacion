class Animal:
    
    def __init__(self, nombre, nPatas):
        self.nombre=nombre
        self.nPatas=nPatas

    def habla(self):
        return ""
    
    
    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.nPatas} patas y sueno así: {self.habla()}"
