'''
problema 2: um elevador de carga possui capacidade para 200kg.
crie um programa que receba do usuario seu peso e o peso da carga
e verifique se a carga esta autorizada a usar o elevador ou não 
'''

peso_do_usuario = float(input('digite seu peso: ').replace(',','.'))
peso_da_carga = float(input('digite o peso da carga: ').replace(',','.'))
peso_total = peso_do_usuario + peso_da_carga
if peso_total > 200:
    print('o peso excede o limite do elevador')
else:
    print('o peso está dentro do limite do elevador')