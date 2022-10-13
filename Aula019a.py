#DICIONÁRIO

#CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA

brasil = []                                             #lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}       #dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}            #dicionário
brasil.append(estado1)
brasil.append(estado2)
print('-='*40)
print(brasil)
print('-='*40)
print(brasil[0])
print('-='*40)
print(brasil[0]['uf'])
print('-='*40)
print(brasil[1]['sigla'])
print('-='*40)
