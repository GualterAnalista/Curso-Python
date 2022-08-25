#LAÇOS DE REPETIÇÃO - PARTE 2
#ESTRUTA DE REPETIÇÃO WHILE

#Comparando o uso de: for x while  - PARTE 2

#Usando o for (Uso para quando sei o limite, neste casdo vai parar no 5)
'''for c in range(1,5):
    n = int(input('Digite um valor:'))
print('Fim')'''

#Usando o while (Nesta situação o programa vai rodar até o usuário digitar N)
#1º EXEMPLO
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r =str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

#2º EXEMPLO
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Acabou!!')'''

#3º EXEMPLO (Saber quantos números digitados foram pares e quantos ímpares
par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #Para não contar o número zero como par na contagem final
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print(f'Você digitou {par} números PARES e {impar} números ÍMPARES!!')