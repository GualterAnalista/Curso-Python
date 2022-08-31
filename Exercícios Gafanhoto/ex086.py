#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos
#pelo teclado.No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):        #letra 'l' de linha
    for c in range(0, 3):    #letra 'c' de coluna
        matriz[l][c] = int(input(f'Digite um valor {l}, {c}: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')  # Os :^5 para centralizar com 5 espaços
    print() #Esse print com a endentação recuada é para quebrar a linha de cada coluna da matriz

