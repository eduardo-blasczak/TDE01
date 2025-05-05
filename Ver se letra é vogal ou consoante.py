listaVogais = ['a', 'e', 'i', 'o', 'u']
while True:
    letraUsuario = input('Digite uma letra: ').lower()
    for letra in letraUsuario:
        if letra in listaVogais:
            print(f'{letra} É uma vogal')
        else:
            print(f'{letra} É consoante')


#ou

#if letraUsuario == 'a' or letraUsuario= 'e' or letraUsuario = 'i' or letraUsuario= 'o' or letraUsuario = 'u':