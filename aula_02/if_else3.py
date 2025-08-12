#variaveis
nome = 'artur'
idade = 12
altura = 1.50

#verifica se a pessoa tem os requisitos mínimos para entrar no parque
if idade >= 12 and altura >= 1.50:
    print(f'{nome} pode entrar no parque')
else:
    print(f'{nome} não pode entrar no parque')

#variáveis
nome = 'artur'
idade = 20

#operador ternário
print(nome, 'é maior de idade' if idade >= 18 else 'é menor de idade')

