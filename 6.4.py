
operacao = int(input("Digite 1 para somar:\nDigite 2 para subtrair:\nDigite 3 para dividir:\nDigite 4 para multiplicar:\n"))

n1 = float((input("Digite o primeiro numero:\n")))
n2 = float((input("Digite o segundo numero:\n")))

if operacao == 1:
    print(n1+n2)

elif operacao == 2:
    print(n1-n2)

elif operacao == 3:
    print(n1/n2)

elif operacao == 4:
    print(n1*n2)

else:
    print("Valor invalido para realizar as operacoes")