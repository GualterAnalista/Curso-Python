valores = [] # ou pode ser assim também:  valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

print('='*35)

#Lendo valores pelo TECLADO
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
#Usando o enumerate: ele pega tanto a chave (índice) quanto o valor
for c, v in enumerate(valores): #Aqui acha-se a chave (índice) de cada elemente da lista
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final lista.')

#"c" de chave (posição do item) e "v" de valor(nome ou nº do item da lista)

