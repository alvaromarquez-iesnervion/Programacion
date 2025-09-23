long_string = "hello everybody"

print(long_string[4]) 
print(long_string[0:-1:2]) #posicion ultima no incluida, con un tercero, saltos
print(long_string.split("e")) #sin nada, usa espacio

words = ["hi", "everybody", "how", "are", "yoy"]
print(" ".join(words))

word1 ="hello".capitalize()
word2 = "Hello"

print(word1 == word2)

print(word1)

print("tenemos una cadena muy larga"[3:14:3])
print("tenemos una cadena muy larga"[::-1])
