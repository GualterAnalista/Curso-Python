n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m,d))
print('A divisão inteira é {} e a potência é {}'.format(di,e))

print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m,d), end=' ') #Vai unir as duas linhas
print('A divisão inteira é {} e a potência é {}'.format(di,e))

print('A soma é {},\no produto é {}\ne a divisão é {:.2f}'.format(s,m,d), end=' ') #Vai saltar linhas
print('A divisão inteira é {}\ne a potência é {}\n'.format(di,e))