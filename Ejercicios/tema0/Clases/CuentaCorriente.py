class CuentaCorriente:
    
    def __init__(self, DNI, saldo):
        self.DNI=DNI
        self.saldo=saldo
        self.nombre= ""

    def _init_(self, DNI, nombre, saldo):
        self.DNI=DNI
        self.saldo=saldo
        self.nombre=nombre

    def sacarDinero(self, dinero):
        if (self.saldo >= dinero):
            self.saldo -= dinero
            print("El dinero se ha retirado correctamente")
        else:
            print("No hay suficiente saldo en la cuenta")

    def ingresarDinero(self, dinero):
        self.saldo+=dinero
    
    def __str__(self):
        cadena= "Nombre: " + self.nombre +"\n"
        cadena+= "DNI: " + self.DNI + "\n"
        cadena += "Saldo" + self.saldo + "\n"
        return cadena
    
    def __eq__(self, otroObjeto):
        equals=False
        if self.DNI==otroObjeto.DNI and self.saldo==otroObjeto.saldo:
            equals=True
        return equals 
    
    def __lt__(self, otroObjeto):
        menor = False
        if self.saldo< otroObjeto.saldo:
            menor=True
        return menor