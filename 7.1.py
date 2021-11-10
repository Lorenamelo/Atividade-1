
lista = ["Lorena", "Antonio", "Sabao", "Lorena", "Antonio", "Sabao", "Lorena", "Antonio", "Sabao"]

conta_nome = {}

for nome in lista:
    if nome not in conta_nome:
        conta_nome[nome] = 0
    conta_nome[nome] += 1

print(conta_nome)