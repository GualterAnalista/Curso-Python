#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
#até 200Km e R$0,45 parta viagens mais longas.

'''
#1ª FORMA
d = float(input('Qual é a distância da sua viagem? '))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print(f'Com a distância de {d:.2f}km, você vai pagar por esta viagem: R$ {preço:.2f}')
'''

#2ª FORMA
d = float(input('Qual é a distância da sua viagem? '))
preço = d * 0.50 if d <= 200 else d * 0.45
print(f'Com a distância de {d:.2f}km,você vai pagar por esta viagem: R$ {preço:.2f}')