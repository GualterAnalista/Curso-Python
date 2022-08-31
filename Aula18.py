#Nessa aula, vamos aprender o que são LISTAS "PARTE 2" e como utilizar listas em Python.
#As listas são variáveis compostas que permitem armazenar vários valores em uma
#estrutura, acessíveis por chaves individuais.

teste = list()
teste.append('Gustavo') #Adicionei à lista o nome 'Gustavo'
teste.append(40)        #Adicionei à lista a idade 40
print(teste)            #Faz a impressão da lista chamada teste
galera = list()         #Criei outra lista com nome de galera
galera.append(teste[:]) #Adicionei a lista teste dentro da lista galera
teste[0] = 'Maria'      #Agora quero acrescentar mais um nome à lista teste dentro da galera
teste[1] = 22
galera.append(teste[:]) #Se não colocar [:] vai duplicar os nomes. Comente esta linha e executa a linha abaixo
#galera.append(teste)
print(galera)           #Faz a impressão da lista galera compondo a lista teste inteira

print('=-'*40)

#OUTRA FORMA DE LISTA COMPOSTA
#Tenho agora 4 estruras compostas dentro de uma grande estrutura
galera =[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])    #Vai mostrar só a lista de João com 19
print(galera[0][0]) #Vai mostrar somente João, pois está na lista 0 e João no índice 1 dessa lista
print(galera[2][1]) #Nesse vai mostar nº 13, pois está na lista 2 e posição 1

print('=-'*40)

for p in galera:    #P/ cada p(pessoa) em galera, mostre os nomes e as idades
    print(p)
print('=-'*40)
for p in galera:    #P/ cada p(pessoa) em galera, mostre só os nomes
    print(p[0])
print('=-'*40)
for p in galera:    #Agora vai mostrar os nomes e idades de maneira formatada
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('=-'*40)
#PEGAR AGORA DADOS DIRETO DO TECLADO DE NOMES E IDADES

galera = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Pegando todos os dados da lista "dados" e adicionando na lista "galera"
    dado.clear()
print(galera)

totmaior = totmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')