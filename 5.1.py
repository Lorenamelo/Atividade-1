
valor = int(input("Digite um valor para deposito! Precisa ser um valor inteiro!\n"))

qtd_notas = 0

while valor > 0:

    if valor >= 100:

        qtd_notas += int (valor / 100)
        valor = valor % 100

    elif valor >= 50 and valor < 100:

        qtd_notas += int (valor / 50)
        valor = valor % 50

    elif valor >= 10 and valor < 50:

        qtd_notas += int (valor / 10)
        valor = valor % 10

    elif valor >= 1 and valor < 10:

        qtd_notas += valor
        valor = 0
    
    else:

        valor = 0
        
print("A quantidade mínima de notas que o banco deve fornecer é ", qtd_notas)
