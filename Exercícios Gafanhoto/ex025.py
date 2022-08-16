#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual seu nome completo? ')).strip()
#print('Seu nome tem Silva? {}'.format('Silva')in nome)
#print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')#no lugar de usar o .format
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')#no lugar de usar o .format