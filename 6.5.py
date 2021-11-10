
numero = int(input("Digite um valor inteiro para ser fatorado:\n"))

while numero >= 1:
    if numero%2 == 0:
        print(int(numero), " | ", 2)
        numero = numero / 2

    elif numero%2 != 0 and numero%3 == 0:
        print(int(numero), " | ", 3)
        numero = numero / 3

    elif numero%2 !=0 and numero%3 != 0 and numero!= 1:
        print(int(numero), " | ", int(numero))
        numero = numero / numero
    else:
        numero = 0
        print("1 | ")
