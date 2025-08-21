import os

while True:
    try:
        #usuario informa o nome do arquivo
        arquivo = input('digite o nome do arquivo (sem extenção): ').strip().lower()

        #abre o arquivo
        with open(f'{arquivo}.txt', 'r', encoding='utf8') as f:
            arquivo_aberto = f.read()
            
        
        os.system('cls' if os.name == 'nt' else 'clear')

        #mostrar dados do arquivo
        print(arquivo_aberto)

        while True:
            prosseguir = input('deseja abrir outro arquivo? (s/n): ').strip().lower()
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('opção inválida')
                continue
        match prosseguir:
            case 's':
                continue
            case 'n':
                break


    except Exception as e:
       print(f'não foi possivel ler o aqrquivo {e}')
       continue