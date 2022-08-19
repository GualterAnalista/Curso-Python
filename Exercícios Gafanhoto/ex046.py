#Faça um programa que mostre na tela uma contagem regressiva para o estouro
#de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print('Vamos iniciar a contagem regressiva em...')
from time import sleep          # O -1 no meio significa que a contagem vai finalizar com 0 (zero)
for c in range(10 , -1, -1):    # O -1 final significa que a contagem será regressiva
    sleep(1)
    print(c)
print('BUM! BUM! POW!')
print('Feliz Ano Novo!!!!')
