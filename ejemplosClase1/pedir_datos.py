user_name= input("introduce your name: ")
print("Your name is", user_name)

age = int(input("Introduce your age: "))
age += 1

print("Your age is:", age)
##print("your age is" + age) no funciona porque el + en este caso concatena solo cadenas y age es un int
print(f"Your age is: {age}")
