import random

lista = []

sair = False

while sair == False:
    nome = input('digite os nomes para o sorteio ou enter para sair')
    if nome != "":
        lista.append(nome)
    else:
        sair = True
escolhido = random.choice(lista)

print('o escolhido foi: ',escolhido)