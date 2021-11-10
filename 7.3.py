
frase = input("Digite uma frase, letras maiusculas apenas nomes proprios:\n")

palavras = frase.split(" ")

#print(palavras)

for palavra in palavras:
    if palavra[0].isupper():
        print(len(palavra)*"*", end=" ")
    else:
        print(palavra, end=" ")
print("\n")