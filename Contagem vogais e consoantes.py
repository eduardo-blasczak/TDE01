palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
contagemvogal = sum(palavra.count(v) for v in vogais)
print(f"O número de vogais é: {contagemvogal}")