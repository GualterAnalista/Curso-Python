#Nessa aula, vamos aprender como criar estruturas condicionais
#aninhadas, usando os comandos if.. elif.. else em programas Python.
                 #ESTRUTURA CONDICIONAL ANINHADA
nome = str(input('Qual é o seu nome? '))
if nome == 'Gualter':
    print('Que nome diferente!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!!!')
print(f'Tenha um bom dia, \033[1;36m{nome}')
