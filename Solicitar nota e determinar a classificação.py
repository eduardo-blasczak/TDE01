#Solicitar nota e determinar a classificação
nota = float(input("Digite sua nota: "))
if  9<= nota <=10:
    print("Sua classificação é A!")
elif 7<= nota <=8.9:
    print("Sua classificação é B!")
elif 5<= nota <=6.9:
    print("Sua classificação é C!")
elif nota <5:
    print("Sua classificação é D!")
else:
    print("Nota inválida!")