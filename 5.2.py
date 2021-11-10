
valor = int(input("Digite um valor em segundos:\n"))

cont = valor

horas = 0
minutos = 0
segundos = 0

while cont > 0:

    if cont >= 3600:
        horas = int (cont / 3600)
        cont = cont % 3600

    elif cont >= 60 and cont < 3600:
        minutos = int (cont / 60)
        cont = cont % 60

    elif cont >= 1 and cont <60:
        segundos = cont
        cont = 0

print("Esse valor equivale a ", horas, " horas, ", minutos, " minutos, ", segundos, " segundos.") 