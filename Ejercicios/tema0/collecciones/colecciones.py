

def pideNumerosConsola(numero):
    listaStrings=[]
    ListaNumeros=[]

    numeros=input("Introduzca los numeros ")
    listaStrings= list(numeros.split(", "))
    listaStrings= list(numeros.split(","))
    listaStrings= list(numeros.split(" "))

    while len(listaStrings) < numero:
        
        print("Debes introducir ", numero, " numeros")
        listaStrings=input("No has introducido suficientes números, introduzca los necesarios " )
    while len(listaStrings) > numero:
        
        print("Debes introducir ", numero, " numeros")
        listaStrings=input("Has introducido demasiados números, introduzca los necesarios " )
    
    for i in listaStrings:
        
        ListaNumeros.append(int(i))
    return ListaNumeros

"""Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 
"""

import random


def crearListaEnterosAleatorios():
    lista=[]
    numero=random.randint(0, 100)
    for i in range(1, 101):
        lista.append(numero)
        numero=random.randint(0, 100)

    return lista

""" Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.
 """
def MaxMinNumerosReales():
    
    ListaNumeros=pideNumerosConsola(10)

    print("El maximo de la lista es ", max(ListaNumeros))
    print("El mínimo de la lista es ", min(ListaNumeros))

"""Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación, recorrerá esa 
tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.
"""

def ParImpar():
    
    ListaNumeros=pideNumerosConsola(8)


    for numero in ListaNumeros:
        if numero % 2==0:
            print(numero, " par")
        else:
            print(numero, " impar")

"""Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.
"""
def OrdenaMayorMenor():
    pass