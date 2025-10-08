class CuentaCorriente:
    
    def __init__(self, DNI, saldo):
        self.DNI=DNI
        self.saldo=saldo
        self.nombre= ""

    def __init__(self, DNI, nombre, saldo):
        self.DNI=DNI
        self.saldo=saldo
        self.nombre=nombre

    def sacarDinero(self, dinero):
        if self.saldo >= dinero:
            self.saldo -= dinero
            return True
        return False


    def ingresarDinero(self, dinero):
        self.saldo+=dinero
    
    def __str__(self):
        cadena= "Nombre: " + self.nombre +"\n"
        cadena+= "DNI: " + self.DNI + "\n"
        cadena += "Saldo: " + self.saldo + "\n"
        return cadena
    
    def __eq__(self, otroObjeto):
     return isinstance(otroObjeto, CuentaCorriente) and self.DNI == otroObjeto.DNI

    
    def __lt__(self, otroObjeto):
        menor = False
        if self.saldo< otroObjeto.saldo:
            menor=True
        return menor