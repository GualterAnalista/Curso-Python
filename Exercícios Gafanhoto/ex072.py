#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
#extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
#e mostrá-lo por extenso e perguntar se deseja continuar.

cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',\
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', \
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if núm >=0 and núm <= 20: #  ou posso usar assim também  0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')
