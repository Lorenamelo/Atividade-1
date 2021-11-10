import math
import numpy

graus = float(input("Digite o valor em graus para um angulo\n"))

#print(type(graus))

graus = numpy.deg2rad(graus)

print(round(graus, 6))

print("Seno ", math.cos(graus))
print("Cosseno ", math.sin(graus))
print("Tangente ", math.tan(graus))