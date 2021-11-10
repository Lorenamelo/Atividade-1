import numpy

n = int(input("Digite um valor:\n"))

vetor = []

for i in range(n):
    vetor.append(i)

vetor = numpy.array(vetor)

print(vetor)
print(vetor.sum())
print(vetor.mean()) 
print(vetor.min())
print(vetor.max())