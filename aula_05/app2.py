import os

while True:
    try:
        # usuario informa o nome do arquivo 
        arquivo = input('digite o nome do arquivo (sem extensao)').strip().lower()

        # abre o arquivo
        with open(f'{arquivo}.txt', 'r', encoding='utf-8') as f:
            arquivoaberto = f.read()
        os.system('cls' if os.name == 'nt' else 'clear')

        # mostrar os dados do arquivo
        print(arquivoaberto)

        while True:
            prosseguir = input('deseja abrir outro arquivo? (s/n)')
            if prosseguir == 's':
                break
            elif prosseguir == 'n':
                break
            else:
                print('opcao invalida')
                continue
    except Exception as e:
        print(f'nao foi possivel abrir o arquivo. {e}')

        SystemExit