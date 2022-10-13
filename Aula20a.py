#CONTINUAÇÃO AULA DE FUNÇÕES COM DEF
#EXPLICAÇÃO 1
a = 3
b = 8
s = a + b
print(s)

a = 9
b = 10
s = a + b
print(s)

a = 7
b = 3
s = a + b
print(s)

print('<>'*15)

#EXPLICAÇÃO 2
#AGORA FAZENDO O MESMO ACIMA UTILIZANDO A FUNÇÃO DEF
#Programa Principal
def soma(a, b): #Tem sempre que dar 2 enter após a montagem do comando "def"
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)

print('<>'*15)

#EXPLICAÇÃO 3
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(4, 5)
soma(8, 9)
soma(2, 1)

