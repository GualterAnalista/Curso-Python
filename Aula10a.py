#CONDIÇÕES - PARTE 1

'''
1ª FORMA
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')
'''

#2ª FORMA - MAIS CORRETA
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo'if tempo <=3 else 'Carro velho')
print('---FIM---')
