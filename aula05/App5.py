# importação
import json

try:
    arquivo = input('digite o nome do arauivo: ').strip().lower()

    with open(f'{arquivo}.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)

        print(f'{'-'*20} DADOS {'-'*20}')
        for dado in dados:
            for chave in dado:
                print(f'{chave.captalize()} : {dado.get(chave)}')
            print('-'*40)
except Exception as e:
    print(f'não foi possivel ler o arquivo.{e}')
    