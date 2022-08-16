#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
#seno, cosseno e tangente desse ângulo.

#1ª FORMA
'''
import math
a = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(a))
print(f'O ângulo de {a:.1f} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(a))
print(f'O ângulo de {a:.1f} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(a))
print(f'O ângulo de {a:.1f} tem o TANGENTE de {tangente:.2f}')
'''

#2ª FORMA
from math import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
seno = sin(radians(a))
print(f'O ângulo de {a:.1f} tem o SENO de {seno:.2f}')
cosseno = cos(radians(a))
print(f'O ângulo de {a:.1f} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(a))
print(f'O ângulo de {a:.1f} tem o TANGENTE de {tangente:.2f}')