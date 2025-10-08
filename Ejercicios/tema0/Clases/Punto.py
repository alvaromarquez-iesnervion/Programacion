from math import *

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def setXY(self, x, y):
        self.x=x
        self.y=y
    
    def desplaza(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def distancia(self, punto):
        distancia=sqrt((self.x-punto.x)**2 + (self.y-punto.y)**2)
        return distancia
    
    def __str__(self):
        return f"({self.x}, {self.y})"
