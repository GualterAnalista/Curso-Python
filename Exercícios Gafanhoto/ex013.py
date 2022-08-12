#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s = float(input('Digite o salário do funcionário: R$ '))
novo = s + (s * 15/100)
print(f'O salário de R$ {s:.2f} com o aumento de 15% vai para R$ {novo:.2f}')
