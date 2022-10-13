#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
#em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter         #para ordenar o randint na posição 1
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6),}
ranking = list()        #O ranking vai ficar em uma lista
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  #Vai colocar em ordem de valor
print('=>='*11)
print('=====RANKING DOS JOGADORES=====')
for i, v in enumerate(ranking): #Para cada índice em valor
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
