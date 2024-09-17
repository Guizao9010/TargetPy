frase = input("Digite uma frase: ")
reversa = ""

for char in frase[::-1]:
    reversa += char

print(reversa)
