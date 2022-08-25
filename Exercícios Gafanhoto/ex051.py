#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

print('='*19)
print('10 TERMOS DE UMA PA')
print('='*19)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (11 - 1) * razão #Para achar o ENÉSIMO termo de uma PA
for c in range(primeiro, décimo, razão):
    print(c, end='->')
print('ACABOU')
