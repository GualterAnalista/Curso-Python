#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 
#2 metros quadrados.

l = float(input('Digite a largura em metros: '))
a = float(input('Digite a altura em metros: '))
area = l * a
print('A sua parede tem {:.2f}m²'.format(area))
print('\nA quantidade de tinta necessária para pintar {:.2f} m² são {:.2f} litros de tinta.\n'.format(area, area / 2))