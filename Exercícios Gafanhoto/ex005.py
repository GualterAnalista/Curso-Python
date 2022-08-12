#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número:\n'))
ns = n + 1
na = n - 1
print('O número digitado foi: {}, seu sucessor é {} e o seu antecessor é {}'.format(n,ns,na))

#Outra forma de fazer ainda melhor utiizando somente uma variável no lugar de 3
print('O número digitado foi: {}, seu sucessor é {} e o seu antecessor é {}'.format(n,(n+1),(n-1)))
