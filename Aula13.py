#REPETIÇÕES EM PYTHON
#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
#que é uma estrutura versátil e simples de entender

#VAMOS REPLICAR A PALAVRA "OI"
'''
for c in range(0,6): #Para repetir "Oi" 6x tem que colocar 0 a 6, pois o último, nº não conta
    print('Oi')
print('FIM')
'''
#VER VÁRIOS EXEMPLOS NO CADERNO NA DATA DE 18/08/2022

#EX. Nº 10

s = 0
for c in range(0,4):
    n = int(input('Digite um valor:'))
    s += n  #ou s = s + n
print(f'O somatório de todos os valores é {s}.')