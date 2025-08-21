import os

while True:
    try:
        novo_texto = input('digite o texto: \n')
        nome_arquivo = input('digite o nome do arquivo (sem extenção): ').strip().lower()

        with open(f'C:\Users\GustavoAzevedoAlfaro\Desktop\logicaprogramacaoaulas\aula05{nome_arquivo}.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear'  )
        print(f'{nome_arquivo}.txt gravado com sucesso')
        
        novo_texto_adicionar = input('digite o novo texto: \n')
        with open(f'C:\Users\GustavoAzevedoAlfaro\Desktop\logicaprogramacaoaulas\aula05{nome_arquivo}.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{novo_texto_adicionar}')
        print('gravado com sucesso')

        with open(f''):

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