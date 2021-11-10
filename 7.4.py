import numpy

vetor1 = []

vetor2 = []

for i in range(3):
    vetor1.append(int(input("Digite um valor para vetor 1\n")))
    vetor2.append(int(input("Digite um valor para vetor 2\n")))

pEscalar = 0

pEscalar = numpy.dot(vetor1, vetor2)
print("Produto Escalar: ", pEscalar)

pVetorial = numpy.cross(vetor1, vetor2)
print("Produto Vetorial: ", pVetorial)