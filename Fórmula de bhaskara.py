#Fórmula de bhaskara 
import math
ValorA = float(input("Digite o valor de A: "))
ValorB = float(input("Digite o valor de B: "))
ValorC = float(input("Digite o valor de C: "))
delta = (ValorB**2)-4*ValorA*ValorC
X1 = ((- ValorB)+(math.sqrt(delta))) / (2*ValorA)
X2 = ((- ValorA)-(math.sqrt(delta))) / (2*ValorB)
print(f"O valor de x é: {X1}")
print(f"O valor de x' é: {X2}")

