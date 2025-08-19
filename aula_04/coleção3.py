'''
from random import randint

print('tente adivinhar o número')
num1 = int(input("digite um número: "))

num_secreto = randint(1,10)
if num1 == num_secreto:
    print('você acertou o numero')
else:
    print('você perdeu')
    print(f'o número era {num_secreto}')
'''

import random

num_secreto = random.randint(1,100)

tentativas = 0
max_tentativas = 10
acertou = False

print(30*'-','bem vindo ao adivinha')
print(f'você tekm {max_tentativas} tentativas para adivinhar o número secreto')

while tentativas < max_tentativas:
    try:
        palpite = int(input('digite o seu palpite: '))

    except ValueError:
        print('você errou, tente novamente')
        continue

    tentativas += 1

    if palpite == num_secreto:
        acertou = True
        break
    elif palpite < num_secreto:
        print('tente um número maior')
    else:
        print('tente um número menor')

if acertou:
    print(f'você acertou o {num_secreto} em {tentativas} tentativas')
else:
    print(f'você não conseguiu acertar o número secreto{num_secreto}')