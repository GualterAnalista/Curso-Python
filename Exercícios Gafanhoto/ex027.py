#Faça um programa que leia o nome completo de uma pessoa, mostrando em
#seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()#Nessa linha vai dividir o nome em pedaços. Um nome em cada bloco de posição
print(nome)#Essa linha nem precisa. Só coloquei para demonstração da lista que será criada
print(f'O seu primeiro nome é: {nome[0]}')
print(f'O seu último nome é: {nome[len(nome)-1]}')#Aqui vai contar tudo e mostrar o último nome
