#INTERROMPENDO REPETIÇÕES WHILE COM O COMANDO BREAK

'''n = s = 0
while True:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n==999:
        break
    s += n
print(f'A soma vale {s}.')'''

#Agora refazendo o Exercício 064 utilizando: "while True" e o "break".
núm = cont = soma = 0
while True:
    núm = int(input('Digite um número [999 para PARAR]: '))
    if núm==999:
        break
    soma += núm
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')


#Abaixo está o Ex064 feito antigo (Feito sem o conhecimento do "While True" e "break")
'''núm = 0
cont = 0
soma = 0  #Posso resumir essas 3 linhas em uma só assim: num = cont = soma = 0
núm = int(input('Digite um número [999 para PARAR]: ')) #Para que o 999 não seja contabilizado
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para PARAR]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')'''