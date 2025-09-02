import json
import os

usuarios = []
novo_arquivo = ''

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
    usuario = {}
    print('1 - cadastrar novo usuario')
    print('2 - salvar arquivo json')
    print('3 - fazer leitura do json')
    print('4 - sair')

    opcao = input('digite sua opçao: ')
   
    match opcao:
        case '1':
            usuario['nome'] = input('digite seu nome: ').strip().title()
            usuario['idade'] = input('digite sua idade: ')
            usuario['email'] = input('digite seu email: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('usuario cadastrado com sucesso')
            continue
        case '2':
            novo_arquivo = input('informe o nome do arquivo: ').strip().lower()
            with open(f'aula_06/{novo_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('arquivo salvo com sucesso')
            continue
        case '3':
            if not novo_arquivo:
                novo_arquivo = input('digite o nome do arquivo: ').strip().lower()
            with open(f'aula_06/{novo_arquivo}.json.', 'r', encoding='utf-8') as f:
                dados = json.load(f)
            print(f'{'-'*20} usuarios {'-'*20}/n')
            for usuarios in dados:
                for chave in dados:
                    print(f'{chave.capitalize()}: {usuario.get(chave)}')
                print('-'*20)
                continue
        case '4':
            print('saindo do sistema')
            break
        case _:
            print('opção inválida')
            continue
