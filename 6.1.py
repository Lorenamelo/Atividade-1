
contador = int (input("Digite um numero para ser o n primeiros numeros da sequencia de Fibonacci\n"))

ultimo = 1
penultimo = 1

print("\n")

if contador == 1:
    print(ultimo, "\n")

elif contador == 2:
    print(ultimo)
    print(penultimo)

elif contador >= 3:

    print(ultimo)
    print(penultimo)

    for contador in range(contador-2):
        numero = ultimo + penultimo
        penultimo = ultimo
        ultimo = numero
        print(numero)

else:
    print("Valor invalido")