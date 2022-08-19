#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirando as notas {n1} e {n2}, a sua média é de: {média:.2f}')
if média < 5:
    print('Você foi REPROVADO!!!')
elif média >= 7:
    print('Você está APROVADO. Parabéns!!! ')
elif média >= 5 and média < 7:   #Pode ser feito também dessa forma:  if 7 > média >= 5:
    print('Você está de RECUPERAÇÃO!!!')

