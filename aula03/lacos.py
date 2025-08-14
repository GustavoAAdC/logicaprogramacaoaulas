#LINK - 18,5 pra baixo, abaixo do peso || entre 18,5 e 24,9, normal || acima de 24,9, acima do peso ||

#ANCHOR - IMC = peso/aktura*altura

print(40*'-', 'CALCULADORA DE IMC',40*'-')
altura = float(input('Digite a sua altura: ').replace(',' , '.'))
peso = float(input('digite o seu peso: ').replace(',' , '.'))


imc = peso/ (altura*altura)

print(f'seu imc é: {imc:.2f}')

if imc <= 18.5:
    print('abaixo do normal')
elif imc <= 24.9:
    print('normal')
elif imc <= 29.9:
    print('sobrepeso')
elif imc <= 34.9:
    print('obesidade grau I')
elif imc <= 39.9:
    print('obesidade grau II')
else:
    print('obesidade grau III')







#LINK -  problema 2: Um elvador de carga possui capacidade para 200kg. Crie um programa que receba do usuario seu peso e o peso da carga e verifica se a carga está autorizada a usar o elevador ou não
print(40*'-', 'CALCULADORA DE SUPORTE DE CARGA',40*'-')
peso_usu = float(input('digite seu peso: ').replace(',' , '.'))
peso_carga = float(input('digite o peso da carga: ').replace(',' , '.'))
limite = 200
peso_total = peso_usu+peso_carga

print(f'O peso total é:{peso_total}')

if peso_total <= limite:
    print('O elevador irá suportar a carga')
else:
    print('O elevador não irá suportar a carga')

print(120*'-')

while True:
    print(40*'-', 'SISTEMA CONSOLE 2ºD', 40*'-')
    print('1 - Calculadora IMC')
    print('2 - maioridade')
    print('3 - calculadora')
    print('4 - dados pessoais')
    print('5 - feliz natal')
    print('6 - sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        pass
    elif opcao == '2':
        pass
    elif opcao == '3':
        while True:
            num1 = float(input('digite o primeiro numero: '))
            num2 = float(input('digite o segundo numero: '))
            print('calculadora')
            print('1 - soma')
            print('2 - divisão')
            print('3 - subtração')
            print('4 - multiplicação')

            opcao_calculo = input('escolha uma operação matemática: ')

            if opcao_calculo == '1':
                print(f'resultado da soma é: {num1 + num2}')
            elif opcao_calculo == '2':
                print(f'resultado da divisão é: {num1/num2}')
            elif opcao_calculo == '3':
                print(f'resultado da subtração é: {num1-num2}')
            elif opcao_calculo == '4':
                print(f'resultado da multiplicação é: {num1*num2}')
            elif opcao_calculo == '5':
                break
            else:
                print('opção invalida')


        ...
    elif opcao == '4':


        nome = input('digite o seu nome: ')
        telefone = input('digite o seu telefone: ')
        cpf = input('digite o seu cpf: ')
        dt_nascimento = input('digite sua data de nascimento: ')
        print(f'| nome: {nome} | telefone: {telefone} | ')
        print(f'| CPF: {cpf} | Data de nascimento: {dt_nascimento}')
        ... 
    elif opcao == '5':
        linhas = 15
        j = 1

        while j<= linhas:
            espacos =linhas - j
            estrelas =2*j-1


            print(' ' * espacos + '*' * estrelas)
            j +=1

    elif opcao == '6':
        break
    else: 
        print('opção invalida')
    

nome1 = 'gustavo'

for i in nome1:
    print(i.replace(i, '*'))
