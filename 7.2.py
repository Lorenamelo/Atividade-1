
lista = []

conta_nome = {}

while True:
    nome = input("Digite um nome:\n")
    if nome: #se tiver um conteudo dentro
        lista.append(nome) #funcao para adicionar o elemento na lista
    else:
        break

for nome in lista:
    if nome not in conta_nome:
        conta_nome[nome] = 0
    conta_nome[nome] += 1

print(conta_nome)