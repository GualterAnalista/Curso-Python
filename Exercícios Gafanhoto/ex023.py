#Faça um programa que leia um número de 0 a 9999 e mostre na tela
#cada um dos dígitos separados.
num = int(input('Informe um número: '))#Vamor usar no exemplo o nº 1234
u = num // 1 % 10#nº/1 depois esse resul. divide por 10 e o u=4 (Que é o resto da divisão por 10)
d = num // 10 % 10#nº/10 depois esse resul. divide por 10 e o d=3 (Que é o resto da divisão por 10)
c = num // 100 % 10#nº/100 depois esse resul. divide por 10 e o c=2 (Que é o resto da divisão por 10)
m = num // 1000 % 10#nº/1000 depois esse resul. divide por 10 e o m=1 (Que é o resto da divisão por 10)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

