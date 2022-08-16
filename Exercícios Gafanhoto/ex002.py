#Faça um programa que leia o nome de uma pessoa e mostre a mensagem de boas vindas.
nome = input('Qual é o seu nome? ')
print('É um prazer te conhecer,', nome,'!')
#ou também pode ser assim:
print('É um prazer te conhecer, {}!'.format(nome))