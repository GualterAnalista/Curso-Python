#Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas
#são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
#acessíveis por chaves individuais.

#TUPLA
num = (2, 5, 9, 1)
print(num)

print('='*30)

#LISTA
num = [2, 5, 9, 1]
num.append(7) #Consigo adicionar mais um valor à LISTA com este comando
num[2] = 3 #Em Lista eu consigo substituir um item por outro, pois LISTA é MUTÁVEL
num.sort() #Vai imprimir a lista em ordem
num.sort(reverse=True) #Nessa linha ele imprime em ordem INVERSA.
num.insert(2, 0) #Insere um valor. Neste caso o nº 0 entra na posição 2 e empurra os outros p/ frente
num.insert(2, 2) #Insere um valor. Neste caso o nº 2 entra na posição 2 e empurra os outros p/ frente
num.remove(2) #Neste caso qual dos 2 será removido? Só o 1º elemento 2


if 4 in num:   #Nessas linhas é p/remover quando encontrar o valor que quer remover
    num.remove(4)
else:
    print('Não achei o número 4')


#num.pop() #Remove o último item da lista. No caso aqui o nº 1 será excluído.
#num.pop(1) #Agora irá remover da lista o item da 1ª posição, que é o nº 5

print(num)
print(f'Essa lista tem {len(num)} elementos') #A função len serve para contar os elementos