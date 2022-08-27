#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
#Brasileiro de Futebol 2022, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time (Escolha um time)

lista = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR',
'Atlético-MG', 'Santos', 'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaçeza',
'Botafogo', 'Ceará', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')

print('='*100)
print(f'Lista de times do Brasileirão 2022: {lista}')
print('='*100)
print(f'Os 5 primeiros são: {lista[0:5]}')
print('='*100)
print(f'Os últimos 4 colocados são: {lista[-4:]}')
print('='*100)
print(f'Lista dos times em Ordem Alfabética: {sorted(lista)}')
print('='*100)
print(f'O Flamengo está na {lista.index("Flamengo")+1}ª posição') #Dentro de {} usa-se aspas duplas

