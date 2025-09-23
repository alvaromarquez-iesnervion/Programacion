from tema0 import *

def test_numbers_between():
    limpiar_consola()
    number1= int(input("Enter your first number "))
    number2= int(input("Enter your first number "))

    numbers_between(number1, number2)

def test_max_of_two():
    limpiar_consola()
    number1= int(input("Enter your first number "))
    number2= int(input("Enter your first number "))

    print("The max is:", max_of_two(number1, number2))

def test_is_vowel():
    limpiar_consola()
    char= input("Enter a letter ")

    if is_vowel(char):
        print("Your letter is a vowel")
    else:
        print("your letter is a consonant")

def test_calculator():
    limpiar_consola()
    number1= float(input("Enter your first number "))
    number2= float(input("Enter your first number "))
    operation=int(input("Enter a number between 1 and 4\n1.addition\n2.subtraction\n3.multiplication\n4.division\n"))

    print("The result is:", calculator(number1, number2, operation))

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
test_calculator()