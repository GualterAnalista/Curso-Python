#Crie um programa que leia o nome de uma cidade. Diga se ela começa ou não
#com o nome “SANTO”.

cid = str(input('Digite o nome de uma cidade: ')).strip()#Para remover espaços indesejáveis
print(cid[:5].upper()=='SANTO')

