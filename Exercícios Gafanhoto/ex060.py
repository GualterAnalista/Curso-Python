#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Exemplo:   5! = 5 x 4 x 3 x 2 x 1 = 120

#1ª FORMA
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O Fatorial de {n} é {f}')'''


#2ª FORMA (Porque nem toda linguagem tem a opção de Factorial igual ao Python.
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1 #Sempre que for multiplicação tem que usar 1 para inicializar ao invés de 0
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c # Ou assim f = f * c
    c -= 1 #Significa que é c (contador) - 1, ou seja, tira 1 unidade do c
print(f'{f}')