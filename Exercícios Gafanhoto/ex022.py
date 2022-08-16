# Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()#Elimina espaços antes e depois do nome completo
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))#Ou fazer linhas abaixo
separa = nome.split()
print(separa)#Só pra ver a lista com os nomes separados
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


