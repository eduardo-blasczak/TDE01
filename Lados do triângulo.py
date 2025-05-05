#Lados do triângulo
LadoA = float(input("Escreva o valor do lado A: "))
LadoB = float(input("Escreva o valor do lado B: "))
LadoC = float(input("Escreva o valor do lado C: "))
if LadoA == LadoB == LadoC:
    print("Triângulo equilátero!")
elif LadoA == LadoB != LadoC:
    print("Triângulo isóceles!")
else:
    print("Triângulo escaleno! ")