print(40*"-", 'CALCULADORA DE IMC' ,40*'-')
altura = float(input('Digite a sua altura: ').replace(',','.'))
peso = float(input('Digite o seu peso: ').replace(',','.'))

imc = peso / (altura * altura)

print()
print(f'Seu IMC é: {imc: .2f}')

if imc <= 18.5:
    print('Abaixo do normal')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade III')