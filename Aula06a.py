#TIPOS PRIMITIVOS E SAÍDAS DE DADOS

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma de', n1, 'e', n2, 'vale', s)  Essa não seria a maneira mais correta e sim a última linha
#print('A soma de {} e {} vale {}'.format(n1,n2,s))
print (f'A soma de {n1} e {n2} é {s}') #Esta é a maneira mais atual de usar o .format