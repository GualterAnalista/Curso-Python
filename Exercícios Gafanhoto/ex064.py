#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
#quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
#números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

núm = 0
cont = 0
soma = 0  #Posso resumir essas 3 linhas em uma só assim: num = cont = soma = 0
núm = int(input('Digite um número [999 para PARAR]: ')) #Para que o 999 não seja contabilizado
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para PARAR]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

