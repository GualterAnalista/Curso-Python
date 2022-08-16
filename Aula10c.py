'''
#1ª FORMA - USANDO A CONDIÇÃO SIMPLES
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi de: {m:.2f}')
print('Parabéns!!! Você foi APROVADO!!!' if m >= 5 else 'Lamento, mas você foi REPROVADO!!')
'''

#2ª FORMA - USANDO A CONDIÇÃO COMPOSTA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi de: {m:.2f}')
if m >= 6.0:   #Não esquecer os dois pontos sempre após o IF e o ELSE
    print('Parabéns!!! Você foi APROVADO!!')
else:
    print('Lamento, mas você foi REPROVADO!!')



