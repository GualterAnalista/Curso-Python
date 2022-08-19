#Crie um programa que mostre na tela todos os números pares que estão
#no intervalo entre 1 e 50.

'''
#1ª FORMA
print('Números pares de 2 a 50:')
for c in range(2,51,2): #Vai contar de 0 a 50 de 2 em 2.
    print(c, end=' ')   # o end=' '  é para deixar em uma única linha c/ espaços entre os nº
print('Fim')
'''

#2ª FORMA
print('Números pares de 2 a 50:')
for c in range(2,51):
    if c % 2 == 0:
        print(c, end=' ')   # o end=' '  é para deixar em uma única linha c/ espaços entre os nº
print('Fim')