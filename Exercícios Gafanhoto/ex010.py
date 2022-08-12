#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quantos reais você tem na carteira: R$ '))
dolar = real / 5.16 #valor do dólar em 12/08/2022
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))