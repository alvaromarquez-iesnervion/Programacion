
class Articulo:
    
    IVA=21

    def __init__(self, nombre, precio, stock ):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def getPVP(self):
        PVP= self.precio + (self.precio*(Articulo.IVA/100))
        return PVP

    def getPVPDescuento(self, descuento):
        descuentoFloat=descuento/100
        PVP=self.getPVP()
        PVPDescuento = PVP - PVP*descuentoFloat
        return PVPDescuento
    
    def vender(self, x):
        posible=False
        if self.stock >= x:
            self.stock -= x
            posible=True
        return posible
    
    def almacenar(self, x):
        self.stock += x

    def __str__(self):
        return f"Artículo: {self.nombre}, Precio: {self.precio:.2f}€, Stock: {self.stock}"

    def __eq__(self, other):
        if isinstance(other, Articulo):
            return self.nombre.lower() == other.nombre.lower()
        return False

    def __lt__(self, other):
        if isinstance(other, Articulo):
            return self.nombre.lower() < other.nombre.lower()
        return NotImplemented