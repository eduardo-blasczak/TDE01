#Cálculo de alíquota
salario = float(input('Digite o seu salário: '))
imposto15 = salario*0.15
imposto25 = salario*0.25
if salario <=20000:
    print("Alíquota não aplicada!")
elif 20001<= salario <=50000:
    print(f'Alíquota aplicada de {imposto15}!')
elif salario >50000:
    print(f"Alíquota aplicada de {imposto25}!")
else:
    print("Valor imcompatível!")

