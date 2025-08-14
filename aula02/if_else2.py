nome = input('digite seu nome:')
idade = int(input('digite sua idade: '))

print('antes do if')
if idade >= 18:
    print('Você é maior de idade')
    print('Você esta dentro do bloco IF')
else:
    print('Você é menor de idade')
    print('Você está no bloco ELSE')
print('Você está fora da estrutura condicional if else')







num1 = 10

if num1 %2 ==0:
    print('nummero par')
else:
    print('numero impar')

print(40*'-','BOLETIM ESCOLAR',40*'-')
nome_aluno = input('insira o nome do aluno: ')
nota1 = float(input('digite a sua 1ª nota: '))
nota2 = float(input('digite a sua 2ª nota: '))
nota3 = float(input('digite a sua 3ª nota: '))
nota4 = float(input('digite a sua 4ª nota: '))
nota5 = float(input('digite a sua 5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/4

# >= 7 aprovado
# >= 5 recuperação
# reprovado

if media >=7:
    print(f'{nome_aluno} aluno aprovado')
    print(f'nota 1: {nota1} | nota 2: {nota2}')
    print(f'nota 3: {nota3} | nota 4: {nota4}')
    print(20*'=')
    print(f'media: {media}')
elif media >=5:
    print(f'{nome_aluno} aluno em recuperação')
    print(f'nota 1: {nota1} | nota 2: {nota2}')
    print(f'nota 3: {nota3} | nota 4: {nota4}')
    print(20*'=')
    print(f'media: {media}')
else:
    print(f'{nome_aluno} aluno reprovado')
    print(f'nota 1: {nota1} | nota 2: {nota2}')
    print(f'nota 3: {nota3} | nota 4: {nota4}')
    print(20*'=')
    print(f'media: {media}')

nome= 'Joao'
Idade2 = 12
Altura = 1.60
if idade >= 12 and altura >= 1.2:
    print(f'A ebtrada de {nome} está autorizada')
else:
    print(f'A entrada de {nome} mão está autorixada')
        

nome2 ='Alex'
idade3 = 39
print(nome, 'é maior de idade.' if idade >=18 else 'é menor de idade')