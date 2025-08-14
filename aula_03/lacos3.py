nome = input('Digite seu nome: ')
cpf = input('Digite o seu cpf: ')
while True: #primeiro ciclo com o true
    #menu principal
    print(50*'-','sistema console 2º ds',50*'-')
    print('1 - calculadora IMC')
    print('2 - maioridade')
    print('3 - calculadora simples')
    print('4 - dados pessoais')
    print('5 - sair')
    opcao = input('digite a opção desejada: ')
    if opcao == '1':
            while True: #<---- true=ciclo, e este ciclo está conectado com o break que quebra o ciclo em baixo, novo ciclo porque o primeiro é do menu principal
                print(40*"-", 'CALCULADORA DE IMC' ,40*'-')
                altura = float(input('Digite a sua altura: ').replace(',','.'))
                peso = float(input('Digite o seu peso: ').replace(',','.'))
                imc = peso / (altura * altura)
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
                opcao = input('Deseja calcular novamente?: ')
                if opcao == ('sim'):
                    continue
                else:
                    break #break que quebra o ciclo2


    elif opcao == "2":
        print(50*'=','MAIORIDADE',50*'=')
        #definindo as variaveis
        ano = 2025
        nasc = int(input('digite seu ano de nascimento: '))
        idade = ano - nasc
        #condições para devolver o valor
        if idade >= 18:
            print('voce é maior de idade')
        else:
            print('voce é menor de idade')
        #solicitando a interação do usuario
        input('Aperte qualquer tecla para voltar para o menu!')
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        pass
    elif opcao == "6":
        pass
