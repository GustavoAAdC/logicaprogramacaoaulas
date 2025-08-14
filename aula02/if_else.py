#
#
#
#
#
#

#FIXME - concatenação com +

nome = "Gustavo" 
idade = 16
altura = 1.74

# saída de dados
print('Olá, meu nome é, ' + nome + ', tenho ' + str(idade) + ' anos de idade')

#FIXME - concatenação com ,
print('Ola, meu nome é,', nome, ',tenho', idade, 'anos de idade')

#FIXME - concatenação format
print('Ola, meu nome é,', {}, ',tenho', {}, 'anos de idade'.format(nome,idade))

#FIXME - concatenação com f-string
print(f'Olá, meu nome é {nome} e tenho {idade} anos de idade')


#eliminando quebra de linha
print(' O Sábio sabia ', end='')
print(' que sabiá sabia assobiar.')


valor = 1.23456789

# exibindo o valor com duas casa depois da virgula
print(f'{valor:,.2f}')

print(50*'=')
peso = input('Digite seu peso: ').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}'.replace('.',','))




#LINK - A1
var_str = "A"
var_int = 20
var_float = 1.2
var_bool = True

print(str(var_str))

print(int(var_int))

print(float(var_float))

print(bool(var_bool))

#LINK - A2
num1 = 12
num2 = 7
soma = num1 + num2

num3 = 15
num4 = 4
resto = num3%num4

num5 = 3
num6 = 2
multiplicacao = num5*num6

print (soma)
print (resto)
print (multiplicacao)

#LINK - A3

print('Bem vindo, por favor, insira seu nome de usuário')
print(50*'=')
nome_us = input('Digite seu nome: ')



#LINK - A4
var2_str = '20'
var2_str = int(var2_str)
print(var2_str + 1)









