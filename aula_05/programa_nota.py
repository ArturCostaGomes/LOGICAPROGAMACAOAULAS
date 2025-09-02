
nome_aluno = input('digite o nome do aluno: ')

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print(f'A média do aluno {nome_aluno} é: {media:.2f}')

if media >= 7:
    print(f'aluno {nome_aluno} arpovado')

else:
    print(f'aluno {nome_aluno} reprovado')
    