nome = input('digite o seu nome: ')
idade = int(input( 'digite a sua idade: '))

print('antes do if')
if idade >= 18:
    print('você é maior de idade')
    print('você está dentro do bloco if')
else:
    print('você é menor de idade')
    print('você está dentro do bloco else')
print('você está fora da estrutura condicional if else')
