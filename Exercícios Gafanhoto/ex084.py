#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) #Vai criar uma ligação entre as duas listas
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='* 30)
print(f'Os dados foram {princ}.')
print(f'Ao total foram cadastradas {len(princ)} pessoas.') #Mostra a quant. de registros.
print(f'O maior peso cadastrado foi de {mai}Kg. Peso de ', end='')
for p in princ: #Para cada pessoa dentro da lista principal...
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi de {men}Kg. Peso de ', end='')
for p in princ: #Para cada pessoa dentro da lista principal...
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()