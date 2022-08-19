#Escreva um programa que pergunte o salário de um funcionário e calcule
#o valor do seu aumento. Para salários superiores a R$1250,00, calcule
#um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual o salário do funcionário? R$ '))
if salário > 1250:
    nsalário = (salário * 10 / 100) + salário #Significa 10% do salário informado
else:
    nsalário = (salário * 15 / 100) + salário
print(f'Seu salário aumentou de R$ {salário:.2f} para R$ {nsalário:.2f}')