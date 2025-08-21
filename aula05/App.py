while True:
    try:
        #entrada de dados
        etanol = float(input('digite digite o preço do etanol: ').replace(',','.'))
        gasolina = float(input('digite digite o preço da gasolina: ').replace(',','.'))
        calculo = (etanol/gasolina)*100
        resultado = 'gasolina' if calculo > 70 else 'etanol'

        print(f'resultado = {calculo:.2f}%. compensa abastacer com {resultado}.')

        opcao = input('deseja refazer o calculo? (s/n)').lower().strip()
        match opcao:
            case 's':
                continue
            case 'n':
                break
            case _:
                print(f'opção inválida')
                continue
    except Exception as e:
        print(f' não foi possivel executar a operação. {e}')
        continue