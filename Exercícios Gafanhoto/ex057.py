#Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente
#até ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    #Nessa linha acima: vai tirar os espaços, vai jogar para maiúscula e vai
    #pegar somente a 1ª letra do que for digitado.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.Por favor, informe seu sexo: ')).strip().upper()[0]
print((f'Sexo {sexo} registrado com sucesso.'))
