#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
#crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
#digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

valores = []
pares = []
ímpares = []

while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Você quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'A lista completa é: {valores} ')
for c, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {ímpares}')
