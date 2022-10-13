#CONTINUANDO COM DICIONÁRIO

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Substitui o [:] fatiamento feito em lista
print(brasil)
for e in brasil: #Para cada estado 'e' em brasil
    for v in e.values():
        print(v, end=' ')
    print()

