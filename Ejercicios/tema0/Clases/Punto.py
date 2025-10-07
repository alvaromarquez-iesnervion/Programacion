class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def setXY(self, x, y):
        self.x=x
        self.y=y
    
    def desplazada(self, dx, dy):
        self.x+=dx
        self.y+=dy