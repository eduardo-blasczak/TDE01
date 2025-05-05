import math 
#Dado um retângulo de lado a=7 e área 63 calcule o valor do lado b.
#fórmula: 7*b=63  portanto 63/7=b
ladoA = float(input("Digite o valor do lado A: "))
Area = float(input("Digite o valor da Area: "))
LadoB = Area/ladoA
print(f"O valor do lado B é: {LadoB}")

#Calculo da diagonal do retângulo
diagonal = math.sqrt((LadoB**2)+(ladoA**2))
print(f"A diagonal do retângulo é: {diagonal}")
