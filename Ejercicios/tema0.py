
import random
import os

def limpiar_consola(): #Funcion que he creado para limpiar la consola antes de una funcion que necesite introducir datos por consola
    os.system('cls')  

"""Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.
"""
def odd_even():

    limpiar_consola()   #limpio la consola 
    number= int(input("Enter a number")) #solicito por consola el número que se va a analizar

    if number % 2 == 0:         #Si el número fuera par, el resto de su division entre 2 sería 0
        print("The number is even")
    else:
        print("the number is odd")

"""Pedir dos números y mostrarlos ordenados de menor a mayor.
"""

def order_numbers(): 

    limpiar_consola()

    number2= int(input("Enter the first number"))   #Solicitud de los números que se van a ordenar
    number1= int("Enter the second number")

    numbers_list= list[number1, number2]    #los meto en una lista que ordeno
    numbers_list.sort
    
    for number in numbers_list: #uso un bucle for para imprimir cada numero separado por coma
        print(number, " ")      

"""Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.
"""

def sum_num():

    limpiar_consola()
    numbers=[]  #Creo una lista en la que ire metiendo los números
    number= int(input("Enter a new positive number")) #solicito el primer numero
    

    while number>=0:    #Mientras el número sea positivo, lo meto en la lista y vuelvo a solicitar otro número
        numbers.append(number)
        number= int(input("Enter a new number or a negative one if you wnat to finish"))

    print("The sumatory of all the numbers is ", sum(numbers))  # cuando el usuario meta un número negativo, salgo del bucle y hago la suma de todos los números de la lista

"""Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). Para ello se introduce por teclado una serie de números, 
para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
"""
def secret_code(): 
    limpiar_consola()
    secret_number= random.randint(1, 100) #genero el número aleatorio entre 1 y 100

    guess=int(input("Guess the secret number or enter -1 to give up")) #solicito el primer intento

    while guess != secret_number or guess != -1 : #mientras el intento no sea el número secreto o -1, sigo pidiendo intentos
        if guess > secret_number: #si el intento es mayor que el número secreto, indico que es menor y vuelvo a solicitar otro intento
            print("lower") 
            guess=int(input("Guess the secret number or enter -1 to give up")) 
        else: #si el intento es menor que el número secreto, indico que es mayor y vuelvo a solicitar otro intento
            print("higher")
            guess=int(input("Guess the secret number or enter -1 to give up"))

    if guess == secret_number: #si el intento es igual al número secreto, felicito al usuario
        print("Congratulations! You guessed the secret number:", secret_number)
    else:  #si el intento es -1, indico que se ha rendido y muestro el número secreto
        print("You gave up. The secret number was:", secret_number)        

"""Escribir una aplicación para aprender a contar, que pedirá un número n y 
mostrará todos los números del 1 al n.
"""

def count_learning(): 
    limpiar_consola()

    number = int(input("Enter a number and learn how to count ")) #solicito el número n

    for i in range(1, number + 1): #uso un bucle for para contar desde 1 hasta n
        print(i, end=", ") #imprimo cada número separado por coma

"""Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
"""

def factorial():
    limpiar_consola()

    number=int(input("Enter the number and you will get its factorial")) #solicito el número
    factorial=1 #inicializo la variable factorial a 1, ya que si la inicializara a 0, el resultado siempre sería 0
    for i in range(1, number + 1): #uso un bucle for para multiplicar todos los números desde 1 hasta n
        factorial *= i
    print("The factorial of", number, "is", factorial) #imprimo el resultado
    
    
"""Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
Un número primo es aquel que sólo es divisible por sí mismo y la unidad.
"""
def prime_number(): 
    limpiar_consola()
    number = int(input("Enter a number: ")) #solicito el número

    if number < 2: #los números menores que 2 no son primos
        print("Your number is not prime")
        return
    is_prime = True #inicializo la variable is_prime a True, y si encuentro un divisor, la cambio a False
    for i in range(2, number): #uso un bucle for para comprobar si el número es divisible por algún número entre 2 y n-1
        if number % i == 0:
            is_prime = False
            break
    if is_prime: #si is_prime sigue siendo True, el número es primo
        print("Your number is prime")
    else: #si is_prime es False, el número no es primo
        print("Your number is not prime")

"""Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *
"""
def triangle(): 
    limpiar_consola()

    size=int(input("Enter the size of your triangle ")) #solicito el tamaño del triángulo
    for i in range(1, size+1): #uso un bucle for para dibujar el triángulo 
        print(" "*(size-i), "* " * i) #imprimo los espacios necesarios para centrar el triángulo y luego imprimo los asteriscos

"""Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. Desde el método main() lee los dos números enteros, 
los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.
"""
def numbers_between(number1 ,number2): 
    
    for i in range(number1+1, number2): #uso un bucle for para imprimir todos los números entre number1 y number2
        print(i, end=", ")


"""Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.
"""

def max_of_two(number1, number2): 
    return max(number1, number2) #uso la función max() para devolver el máximo de los dos números

"""Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.
"""

def is_vowel(char):
    result= bool
    if char in "aeiouAEIOU": #si el carácter está en la cadena de vocales, devuelvo True, si no, False
        result=True
    else:
        result=False    
        
    return result

"""Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. Las operaciones 
disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 
para la división. La función devolverá el resultado de la operación mediante un número real.
"""

def calculator(number1:float , number2:float, operation:int):

    result=float #inicializo la variable result como float para que pueda devolver números decimales en caso de ser necesario

    if operation==1: # si la operación es 1, sumo los dos números
        result= number1 + number2
    elif operation==2: # si la operación es 2, resto los dos números
        result= number1 - number2
    elif operation == 3: # si la operación es 3, multiplico los dos números
        result= number1 * number2
    elif operation == 4: # si la operación es 4, divido los dos números 
        result= number1 / number2
    else: # si la operación no es ninguna de las anteriores, indico que no es válida
        print("operation not valid")
    return result