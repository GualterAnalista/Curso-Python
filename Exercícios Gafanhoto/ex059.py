#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar  [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>>>>Qual é a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é = {soma}.')
    elif opção == 2:
        mult = n1 * n2
        print(f'O resultado entre {n1} x {n2} é = {mult}.')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é = {maior}.')
        else:
            n1 == n2
            print(f'Os números {n1} e {n2} são IGUAIS. Não existe maior entre eles!!')
    elif opção ==4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção Inválida! Tente novamente!')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!!')
