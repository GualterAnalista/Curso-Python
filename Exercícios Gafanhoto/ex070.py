#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
#perguntar se o usuário vai continuar ou não. No final, mostre:

total = totmil = menor = cont =0
barato = ' '
print('-='*10)
print('LOJA SUPER BARATÃO')
print('-='*10)
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil +=1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
       break
#print('Fim')
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi de R$ {total:.2f}.')
print(f'Temos mais de {totmil} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi \33[34m{barato.upper()} \33[mque custa R$ {menor:.2f}')
