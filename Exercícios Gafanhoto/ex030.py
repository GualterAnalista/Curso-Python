#Crie um programa que leia um número inteiro e mostre na tela se
#ele é PAR ou ÍMPAR.

valor = int(input('Digite um número para saber se ele é par ou ímpar: '))
print(f'O número {valor} é PAR' if valor % 2 == 0 else f'O número {valor} é ÍMPAR')