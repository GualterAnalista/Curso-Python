#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

'''
#1ª FORMA
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')
'''


#2ª FORMA
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')
