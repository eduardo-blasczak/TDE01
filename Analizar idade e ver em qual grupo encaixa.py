#Analizar idade e ver em qual grupo encaixa
idade = int(input("Digite sua idade: "))
if idade >=0 and idade <=12:
    print("Você é uma criança!")
elif idade >12 and idade <18:
    print("Você é um adolescente!")
elif idade >=18 and idade <=59:
    print("Você é adulto!")
elif idade >=60:
    print("Você é idoso!")
