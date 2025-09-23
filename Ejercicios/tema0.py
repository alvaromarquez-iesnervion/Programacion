
import random
import os

def limpiar_consola():
    os.system('cls')  

"""Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.
"""
def odd_even():

    limpiar_consola()
    number= int(input("Enter a number"))

    if number % 2 == 0:
        print("The number is even")
    else:
        print("the number is odd")

"""Pedir dos números y mostrarlos ordenados de menor a mayor.
"""

def order_numbers(): 

    limpiar_consola()
    number2= int(input("Enter the first number"))
    number1= int("Enter the second number")

    numbers_list= list[number1, number2]

    numbers_list.sort
    
    for number in numbers_list:
        print(number, " ")

"""Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.
"""

def sum_num():

    limpiar_consola()
    numbers=[]
    number= int(input("Enter a new positive number"))
    

    while number>=0:
        numbers.append(number)
        number= int(input("Enter a new number or a negative one if you wnat to finish"))

    print("The sumatory of all teh numbers is ", sum(numbers))

"""Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). Para ello se introduce por teclado una serie de números, 
para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
"""
def secret_code():
    limpiar_consola()
    secret_number= random.randint(1, 100)

    guess=int(input("Guess the secret number or enter -1 to give up"))

    while guess != secret_number or guess != -1 :
        if guess > secret_number:
            print("lower")
            guess=int(input("Guess the secret number or enter -1 to give up"))
        else:
            print("higher")
            guess=int(input("Guess the secret number or enter -1 to give up"))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number:", secret_number)
    else:
        print("You gave up. The secret number was:", secret_number)        

"""Escribir una aplicación para aprender a contar, que pedirá un número n y 
mostrará todos los números del 1 al n.
"""

def count_learning():
    limpiar_consola()

    number = int(input("Enter a number and learn how to count "))

    for i in range(1, number + 1):
        print(i, end=", ")

"""Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
"""

def factorial():
    limpiar_consola()

    number=int(input("Enter the number and you will get its factorial"))
    factorial=1
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is", factorial)
    
    
"""Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
Un número primo es aquel que sólo es divisible por sí mismo y la unidad.
"""
def prime_number():
    limpiar_consola()
    number = int(input("Enter a number: "))

    if number < 2:
        print("Your number is not prime")
        return
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Your number is prime")
    else:
        print("Your number is not prime")

"""Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *
"""
def triangle():
    limpiar_consola()

    size=int(input("Enter the size of your triangle "))
    for i in range(1, size+1):
        print(" "*(size-i), "* " * i)

"""Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. Desde el método main() lee los dos números enteros, 
los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.
"""
def numbers_between(number1 ,number2):
    
    for i in range(number1+1, number2):
        print(i, end=", ")


"""Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.
"""

def max_of_two(number1, number2):
    return max(number1, number2)

"""Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.
"""

def is_vowel(char):
    result= bool
    if char in "aeiou":
        result=True
    else:
        result=False    
        
    return result

"""Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. Las operaciones 
disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 
para la división. La función devolverá el resultado de la operación mediante un número real.
"""

def calculator(number1:float , number2:float, operation:int):

    result=float

    if operation==1:
        result= number1 + number2
    elif operation==2:
        result= number1 - number2
    elif operation == 3:
        result= number1 * number2
    elif operation == 4:
        result= number1 / number2
    else:
        print("operation not valid")
    return result