#Escreva um programa em Python que leia um número inteiro qualquer e
#peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para a conversão que deseja:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{opção} convertido para BINÁRIO é igual a {bin(num)[2:]}')#Esse [2:] remove números à esquerda
elif opção == 2:
    print(f'{opção} convertido em OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{opção} convertido em HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção INVÁLIDA!!!')
