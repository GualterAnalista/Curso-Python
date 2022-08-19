#Crie um programa que faça o computador jogar Jokenpô com você (Pedra, Papel e Tesoura)

from random import randint
from time import sleep
print('-='*25)
print('Vamos brincar de PEDRA, PAPEL E TESOURA?')
print('-='*25)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print('Escolha uma das opções:')
print('''[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print(f'O computador escolheu {(itens[computador])}')
print(f'O jogador escolheu {(itens[jogador])}')
print('-='*15)
if computador == 0:     #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida!!!')
elif computador == 1:   #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida!!!')
elif computador == 2:   #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!!!')






