#Escreva um programa para aprovar o empréstimo bancário para a compra de
#uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
#anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
#então o empréstimo será negado.

casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salário = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos quer financiar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação ', end='')#Quebrar a linha
print(f'será de R$ {prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!!!')