#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
#os 10 primeiros termos da progressão usando a estrutura while.

#USANDO A ESTRUTURA for
'''print('='*19)
print('10 TERMOS DE UMA PA')
print('='*19)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (11 - 1) * razão #Para achar o ENÉSIMO termo de uma PA
for c in range(primeiro, décimo, razão):
    print(c, end='->')
print('ACABOU')'''


#USANDO A ESTRUTURA while
print('='*10)
print('GERADOR DE PA')
print('='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end='->')
    termo += razão
    cont += 1
print('ACABOU')