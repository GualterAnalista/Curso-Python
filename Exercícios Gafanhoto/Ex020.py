#Sorteando uma ordem na lista. O mesmo professor do desafio 19 quer
#sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada.

#1ª FORMA
'''
import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)#Usado p/ dar uma embaralhada na lista digitada pelo usuário
print('A ordem de apresentação sera:')
print(lista)
'''

#2ª FORMA

from random import shuffle
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)#Usado p/ dar uma embaralhada na lista digitada pelo usuário
print('A ordem de apresentação sera:')
print(lista)