#Desconto aplicável
valorcompra = float(input("Digite o valor da sua compra: "))
desconto = valorcompra*0.1
valorfinal = valorcompra+desconto
if valorcompra > 100:
    print(f"Seu desconto será de: {desconto}")
    print(f"Valor final: {valorfinal}")
else:
    print("Valor não elegível para desconto!")
    
