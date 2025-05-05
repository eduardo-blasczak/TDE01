#Disponibilidade para CNH
idade = float(input("Digite a sua idade: "))
if idade >=18:
    print("Você é maior de idade!")
    if idade >=21:
        print("Você é elegível para obter sua habilitação!")
    else:
        print("Você não é elegível para obter sua habilitação!")
else:
    print("Você é menor de idade!")
