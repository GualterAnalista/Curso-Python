#Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
#As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores
#em uma mesma estrutura, acessíveis por chaves individuais.

#1º EXEMPLO DE CRIAÇÃO DE TUPLAS

print('='*25)
#POSIÇÃO:      0         1        2        3           4
lanche = 'Humburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita' #A Tupla pode ter ou não PARÊNTESES
print(lanche) #Assim ele imprime todo o GRUPO
print(lanche[1]) #Assim ele imprimie somente a variável que estiver na posição solicitada(Suco).
print(lanche[3]) #Aqui será impresso PUDIM
print(lanche[0]) #Aqui será impresso HUMBURGUER
print(lanche[-3]) #Agora imprime de trás para frente, ou seja, será impresso PUDIM
print(lanche[-2])#Imprime PIZZA
print(lanche[1:3]) #Vai imprimir SUCO, PIZZA. Não vai PUDIM porque o último nº é ignorado
print(lanche[2:]) #Imprime da posição 2 até o final, ou seja, PIZZA e PUDIM
print(lanche[:2]) #Agora do início até posição 1, pois ignora o último.
print(lanche[-2:]) #Começa em PIZZA e vai até PUDIM
print(lanche[-3:]) #Começa em SUCO, PIZZA e PUDIM, pois sai de trás pra frente
print(len(lanche)) #Nessa linha aparece o nº 4, pois mostra a quantidade de itens na Tupla

print('='*25)

#USANDO O FOR - PARTE 1 = Esta é a maneira mais CLÁSSICA e a mais usada
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!!!')

print('='*25)

#USANDO O FOR - PARTE 2 = Consigo ver também a posição de cada elemento
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!!!')

print('='*25)

#USANDO O FOR - PARTE 3 = Consigo ver também a posição de cada elemento usando o ENUMERATE
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!!!')

print('='*25)

#AGORA VAMOS USAR UM MÉTODO CHAMADO SORTED (SIGNIFICA ORGANIZADO EM ORDEM ALFABÉTICA)
#Essa função sorted mosta o lanche em ordem alfabética, mas não muda as posições originais
print(sorted(lanche))

print('='*25)

#OUTRA FUNCIONALIDADE COM A TUPLA (UNIR VARIÁVEIS)
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(a)
print(b)
print(c)
print(len(c)) #Vai dizer quantos elementos tem na variável c
print(c.count(5)) #Significa perguntar quantas vezes aparece o nº 5 dentro de c
print(c.index(8)) #Significa perguntar em que posição está o nº 8 em c. Nesse exemplo vai aparecer posição 1
print(c.index(5, 1)) #Vai mostrar o próximo nº 5 na posição 1 dele. Ele está na posiçã 0 e posição 5.

print('='*25)

#MAIS EXEMPLOS COM TUPLA
pessoa = ('Guastavo', 39, 'M', 99.88) #Posso ter dados de tipos diferentes dentro das tuplas
print(pessoa)
#del(pessoa) Com esse comando eu apago a variável inteira.



