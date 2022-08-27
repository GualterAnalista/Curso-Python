#REVISÃO DE EXERCÍCIOS
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
#mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listanum = []
maior = menor = 0
for p in range(0, 5):
    listanum.append(int(input(f'Digite uma valor para a posição {p}: ')))
    if p == 0:
        maior = menor = listanum[p]
    else:
        if listanum[p] > maior:
            maior = listanum[p]
        if listanum[p] < menor:
            menor = listanum[p]
print(f'O maior valor foi: {maior} nas posições: ', end='')
for p, v in enumerate(listanum):
    if v == maior:
        print(f'{p}...', end='')
print(f'\nO menor valor foi: {menor} nas posições: ', end='')
for p, v in enumerate(listanum):
    if v == menor:
        print(f'{p}...', end='')
print(f'\nOs valores foram: {listanum}')