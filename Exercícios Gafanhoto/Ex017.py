#Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triângulo retângulo. Calcule e mostre o comprimento da
#hipotenusa.
#1ª FORMA
'''
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2)
hi = float(input(f'A hipotenusa vai medir: {hi:.2f}'))
'''

#2ª FORMA
'''
import math
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir: {hi:.2f}')
'''

#3ª FORMA
from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(co,ca)
print(f'A hipotenusa vai medir: {hi:.2f}')