from Ejercicios.tema0.tema0 import *

def test_numbers_between(): #función para probar numbers_between
    limpiar_consola()
    number1= int(input("Enter your first number ")) #solicito los dos números
    number2= int(input("Enter your first number ")) 

    numbers_between(number1, number2) #llamo a la función numbers_between con los dos números como parámetros

def test_max_of_two(): #función para probar max_of_two
    limpiar_consola()
    number1= int(input("Enter your first number ")) #solicito los dos números
    number2= int(input("Enter your first number "))

    print("The max is:", max_of_two(number1, number2))  #imprimo el resultado de la función max_of_two con los dos números como parámetros

def test_is_vowel(): #función para probar is_vowel
    limpiar_consola()
    char= input("Enter a letter ") #solicito el carácter

    if is_vowel(char): #si la función is_vowel devuelve True, el carácter es una vocal
        print("Your letter is a vowel")
    else: #si la función is_vowel devuelve False, el carácter es una consonante
        print("your letter is a consonant")

def test_calculator(): #función para probar calculator
    limpiar_consola()
    number1= float(input("Enter your first number ")) #solicito los dos números y la operación
    number2= float(input("Enter your first number "))
    operation=int(input("Enter a number between 1 and 4\n1.addition\n2.subtraction\n3.multiplication\n4.division\n"))

    print("The result is:", calculator(number1, number2, operation)) #imprimo el resultado de la función calculator con los dos números y la operación como parámetros

#descomentar para probar la función

#odd_even()
#order_numbers() 
#sum_num() 
#secret_code() 
#count_learning() 
#factorial() 
#prime_number() 
#triangle() 
#test_numbers_between() 
#test_max_of_two()
#test_is_vowel()
#test_calculator()