#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual é o preço do produto: R$ '))
novo = preço - (preço * 5 / 100)
print('\nO produto que custava R${:.2f}, com a promoção de 5% de desconto vai para R${:.2f}\n'.format(preço, novo))
