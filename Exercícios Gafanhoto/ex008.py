#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
mt = float(input('Digite uma distância em metros: '))
cm = mt * 100
mm = mt * 1000
print('O valor de {:.2f} metros é igual a {:.2f} centímetros e igual a {:.2f} milímetros'.format(mt, cm, mm))
