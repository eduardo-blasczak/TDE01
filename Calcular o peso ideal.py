#Calcular o peso ideal
altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))
sexo = input("Digite M para masculino ou F para feminino: ").upper()

if sexo.startswith("M"):
    peso = (peso * altura) - 58
    print(f"Seu peso ideal é: {peso}")
elif sexo.startswith("F"):
    peso = (peso * altura) - 44.
    print(f"Seu peso ideal é: {peso}")
else:
    print("Informe seu sexo corretamente")