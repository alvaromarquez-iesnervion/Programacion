
import re

def pideNumerosConsola(numero): 

    listaStrings=[] 
    listaNumeros=[] 

    print("debes introducir ", numero, "numeros") 
    numeros=input("Introduzca los numeros ") 
    numeros=numeros.strip()
    listaStrings= list(numeros.split(", ")) 
    listaStrings= list(numeros.split(",")) 
    listaStrings= list(numeros.split(" "))

    while len(listaStrings) < numero: 
        print("Debes introducir ", numero, " numeros") 
        numeros=input("No has introducido suficientes números, introduzca los necesarios " ) 
        numeros=numeros.strip()
        listaStrings= list(numeros.split(", ")) 
        listaStrings= list(numeros.split(",")) 
        listaStrings= list(numeros.split(" "))
    
    while len(listaStrings) > numero: 
        print("Debes introducir ", numero, " numeros") 
        numeros=input("No has introducido suficientes números, introduzca los necesarios " )
        numeros=numeros.strip() 
        listaStrings= list(numeros.split(", ")) 
        listaStrings= list(numeros.split(",")) 
        listaStrings= list(numeros.split(" "))   

    for i in listaStrings: 
        listaNumeros.append(int(i)) 
    
    return listaNumeros
        
            


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
    ListaNumeros= pideNumerosConsola(10)
    ListaNumeros.sort(reverse=True)
    for numero in ListaNumeros:
        print(numero, end=", ")

"""Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10. 
Luego pedirá un valor N y mostrará cuántas veces aparece N. 
"""
def CuentaVecesN():
    listaNumeros=[]
    for i in range(1, 101):
        listaNumeros.append(random.randint(1, 10))
    n=int(input("Que numero quieres revisar cuantas veces sale en la lista? "))

    numeroVeces=0
    
    for numero in listaNumeros:
        if n==numero:
            numeroVeces += 1

    print("El número ", n, "aparece ", numeroVeces, "veces")

"""Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.
"""

def CuentaPalabrasDiccionario():
    texto = input("Introduce un texto ")
    texto= texto.strip()
    texto = texto.replace(",", "").replace(".", "")
    listaPalabras = list(texto.split())
   
    
    diccionarioPalabras = {}
    
    for palabra in listaPalabras:
        if palabra not in diccionarioPalabras:
            numeroVeces= listaPalabras.count(palabra)
            diccionarioPalabras[palabra]= numeroVeces
    print(diccionarioPalabras)
        
"""Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. 
La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.
"""
def VerContactos(contactos:dict):
    for nombre in contactos:
        numero=contactos[nombre]
        print(nombre,": " , numero)

def EliminarContacto(contacto:str, contactos:dict):
    if contacto in contactos:
        del contactos[contacto]

def BuscarContacto(contacto:str, contactos:dict):
    return print(contacto, contactos[contacto])

def AñadeContacto(contacto:str, numero:int,contactos:dict):
    if contacto not in contactos:
        contactos[contacto]= numero

def Contactos():
    contactos = {"Alvaro": 665101268, "Manuel": 633120033}

    while True:
        print("\n--- Menú de Contactos ---")
        print("1. Ver contactos")
        print("2. Añadir contacto")
        print("3. Eliminar contacto")
        print("4. Buscar contacto")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            VerContactos(contactos)

        elif opcion == "2":
            nombre = input("Introduce el nombre: ")
            numero = input("Introduce el número: ")
            if numero.isdigit():
                AñadeContacto(nombre, int(numero), contactos)
            else:
                print("El número debe ser numérico.")

        elif opcion == "3":
            nombre = input("Introduce el nombre a eliminar: ")
            EliminarContacto(nombre, contactos)

        elif opcion == "4":
            nombre = input("Introduce el nombre a buscar: ")
            if nombre in contactos:
                BuscarContacto(nombre, contactos)
            else:
                print("Ese contacto no existe.")

        elif opcion == "5":
            print("Saliendo de la agenda...")
            break

        else:
            print("Opción no válida, prueba otra vez.")
    
"""Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres de los productos y los valores son las cantidades vendidas. 
El programa debe permitir al usuario agregar nuevas ventas y calcular el total de ventas para un producto específico. Implementa un menú con ambas opciones. 
"""
def AñadeVenta(producto:str, ventas:int, ventasProductos:dict):
    ventasProductos[producto]= ventas + ventasProductos.get(producto, 0)
    
def CalculaVentas(producto:str, ventasProductos:dict):
    return ventasProductos[producto]

def Ventas():

    ventasProductos=dict()

    while True:
        print("\n---Selecciona una opción---")
        print("1.Añade venta")
        print("2. Calcula ventas")
        print("3. Salir")

        opcion=int(input("Elije una de las opciones "))

        if opcion == 1:
            producto=input("introduce el nombre del producto ")
            ventas=input("introduce las unidades vendidas de ese producto ")
            if ventas.isdigit():
                
                AñadeVenta(producto, int(ventas), ventasProductos)
            else:
                print("El numero de ventas debe ser un número ")

        elif opcion == 2:
            producto=input("Introduce el nombre del producto cuyas ventas quieres visualizar ")
            print(CalculaVentas(producto, ventasProductos))

        elif opcion == 3:
            break
        else:
            print("Opcion incorrecta ")

"""Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación para cada letra, como en el Scrabble. 
El programa le pedirá una palabra al usuario y se mostrará por pantalla la puntuación que tiene la palabra en total."""

def generarDiccionarioScrabble():
    puntuaciones = {
        1: ["A", "E", "O", "S", "I", "U", "N", "L", "R", "T"],
        2: ["C", "D", "G"],
        3: ["M", "B", "P"],
        4: ["F", "H", "V", "Y"],
        5: ["CH", "Q"],
        8: ["J", "LL", "Ñ", "RR", "X"],
        10: ["Z"]
    }

    diccionario = {}
    for puntos, letras in puntuaciones.items():
        for letra in letras:
            diccionario[letra] = puntos

    return diccionario

def CalculaPuntuacionScribble():
    palabra=input("Introduzca la palabra a la que quieres calcularle la puntuacion ")
    palabra=palabra.upper()
    puntuaciones= generarDiccionarioScrabble()
    puntuacion=0
    for letra in palabra:
        puntuacion += puntuaciones[letra]

    print("tu puntuacion es: ", puntuacion)

"""Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
conjunto 1:
e i k m p q r s t u v
conjunto 2: 
p v i u m t e r k q s

El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, cada vez que encuentre en la frase una letra del conjunto 1 
la sustituirá por su correspondiente en el conjunto 2.
"""
def EncriptarFrase():
    diccionario = {"e": "p", "i": "v", "k": "i", "m": "u", "p": "m", "q": "t", "r": "e", "s": "r", "t": "k", "u": "q", "v": "s"}

    frase=input("introduzca la frase que quieres encriptar: ")
    encriptada = ""
    for letra in frase:
        encriptada += diccionario.get(letra, letra)
    print("tu palabra encriptada es. ", encriptada)