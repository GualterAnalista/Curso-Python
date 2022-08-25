#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for

'''
#1ª FORMA
n = int(input('Digite um número e veja a sua tabuada: '))
print('-'*12)
for c in range(1,11):
    res = n * c
    print(f'{n} x {c} = {res}')
print('-'*12)
'''



#2ª FORMA
n = int(input('Digite um número e veja a sua tabuada: '))
print('-'*12)
for c in range(1,11):
   print(f'{n} x {c} = {n * c}')
print('-'*12)