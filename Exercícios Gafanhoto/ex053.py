#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.
#Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

#DETECTOR DE PALÍNDROMO

'''
#1ª FORMA
frase = str(input('Digite uma frase: ')).strip().upper() #Tira os espaços e joga tudo p/ maiúscula
palavras = frase.split() #irá pegar a frase digitada e colocar em blocos
junto = ''.join(palavras) #esta linha vai juntar toda a frase sem nenhm espaço entre as palavras
print(f'Você digitou a frase {junto}')
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um PALÍNDROMO!!')
else:
    print('A frase digitada não é um PALÍNDROMO')
'''


#2ª FORMA (SEM USAR O FOR)
frase = str(input('Digite uma frase: ')).strip().upper() #Tira os espaços e joga tudo p/ maiúscula
palavras = frase.split() #irá pegar a frase digitada e colocar em blocos
junto = ''.join(palavras) #esta linha vai juntar toda a frase sem nenhm espaço entre as palavras
print(f'Você digitou a frase {junto}')
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um PALÍNDROMO!!')
else:
    print('A frase digitada não é um PALÍNDROMO')