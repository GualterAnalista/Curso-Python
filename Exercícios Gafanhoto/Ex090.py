#Faça um programa que leia nome e média de um aluno, guardando também a situação
#em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}  #Ou pode ser assim: aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*35)
for k, v in aluno.items():      #Para cada chave(k) e valor(v) em alunos fazer:
    print(f'  - {k} é igual {v}')