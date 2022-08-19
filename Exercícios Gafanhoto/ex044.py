#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('{:=^30}'.format('ZIP CELL'))
valor = float(input('Qual o valor do produto? R$ '))
print('-='*18)
print('   ESCOLHA A FORMA DE PAGAMENTO')
print('-='*18)
print('''[1] - à vista dinheiro/cheque
[2] - à vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    novo = valor - (valor * 10/100)
elif opção == 2:
    novo = valor - (valor * 5/100)
elif opção == 3:
    novo = valor
    dividido = novo / 2
    print(f'Sua compra será parcelada em 2x de R$ {dividido:.2f} sem juros.')
elif opção == 4:
    novo = valor + (valor * 20/100)
    parcelas = int(input('Quantas parcelas? '))
    dividido = novo / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {dividido:.2f} com juros.')
else:
    novo = valor
    print('Opção INVÁLIDA de pagamento!!! Tente novamente.')
print(f'Sua compra de {valor:.2f} vai custar R$ {novo:.2f} no final.')