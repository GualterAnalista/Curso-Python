#IMPORTANDO SOMENTE A BIBLIOTECA DE RAIZ
from math import sqrt,floor #Não esquecer da vírgula entre sqrt e floor
num = int(input('Digite um número: '))
raiz = sqrt(num) #Aí eu não preciso usar a função math nessa linha
#print(f'A raiz de {num:.2f} é {raiz:.2f}')#Se quiser usar de forma arredondada
#print(f'A raiz de {num:.2f} é {math.ceil(raiz)}')#Arredondando para cima
print(f'A raiz de {num:.2f} é {floor(raiz)}')#Arredondando para baixo