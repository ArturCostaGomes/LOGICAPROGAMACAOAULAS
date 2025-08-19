'''
conjunto_numérico = ['1', '2', '3', '4', '5'] #variável só com com vários valores, pode ser números, etc
print(conjunto_numérico[2])#printando um valor específico dessa variável que tem multiplos valores, especificando qual valor eu quero com o [x]
print(conjunto_numérico[0])# 0 é primeiro valor desse conjunto, no caso é o número
'''
'''
nomes = ['fulano', 'ciclano', 'beltano', 'maria']
nomes[0] = 'alex' #escolhi o primeiro termo(0)e troquei por outro valor(alex)
print(nomes[0])
'''
'''
print("'fulano', 'ciclano', 'beltano', 'maria'")
lista = ['fulano', 'ciclano', 'beltano', 'maria']
lista_trocada = input('informe o nome que deseja alterar: ')
lista[lista.index(lista_trocada)] = input('digite o novo nome: ')
for nome in lista:
    print(nome)
''' 
'''
import os
from time import sleep


cont = input('digite um número inteiro: ')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'contagem regressiva: {cont_int}')
        sleep(1)
        cont_int -= 1
except:
    print('digite um número válido')
print('fim da contagem')
'''
'''
import random
nome1 = input("digite o primeiro nome: ")
nome2 = input("digite o segundo nome: ")
nome3 = input("digite o terceiro nome: ")
nome4 = input("digite o quarto nome: ")
nome5 = input("digite o quinto nome: ")
lista = [nome1, nome2, nome3, nome4, nome5]
escolhido = random.choice(lista)
'''