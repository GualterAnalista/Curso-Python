#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
c = float(input('Digite a temperatura em graus Celsius: '))
f = c * 1.8 + 32
print(f'A temperatura de {c:.2f}º Celsius é igual a {f:.1f}º Fahrenheit')