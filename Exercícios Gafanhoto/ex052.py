#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


#1ª FORMA
'''núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end='')
print('\n\033[m'f'O número {núm} foi dividido {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!!!')
else:
    print('E por isso ele NÃO É PRIMO!!!')
'''

#2ª FORMA (Usando a biblioteca Colorama para colocar cores)
from colorama import Fore, Style
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print(Fore.RED + '', end=' ')
        tot += 1
    else:
        print(Fore.GREEN+'', end=' ')
    print(c, end='')
print(Fore.CYAN+f'\nO número {núm} foi dividido {tot} vezes')
print(Style.RESET_ALL, end='')
print(Fore.YELLOW, end='')
if tot == 2:
    print('E por isso ele É PRIMO!!!')
else:
    print('E por isso ele NÃO É PRIMO!!!')


