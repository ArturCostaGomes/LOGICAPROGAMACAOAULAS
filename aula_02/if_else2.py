print(40*'-','boletem escolar' ,40*'-')

nome_aluno = input('digite o nome do aluno: ')

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
nota4 = float(input('digite a quarta nota: '))
nota5 = float(input('digite a quinta nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f'A média do aluno {nome_aluno} é: {media:.2f}')

if media >= 7:
    print(f'{nome_aluno} aluno arpovado')
    print(f'nota 1: {nota1} | nota 2: {nota2}')
    print(f'nota 3: {nota3} | nota 4: {nota4}')
    print(f'nota 5: {nota5}')

elif media >= 5:
    print(f'{nome_aluno} aluno em recuperação')
    print(f'nota 1: {nota1} | nota 2: {nota2}')
    print(f'nota 3: {nota3} | nota 4: {nota4}')
    print(f'nota 5: {nota5}')
else:
    print(f'{nome_aluno} aluno reprovado')
    print(f'nota 1: {nota1} | nota 2: {nota2}')
    print(f'nota 3: {nota3} | nota 4: {nota4}')
    print(f'nota 5: {nota5}')
    