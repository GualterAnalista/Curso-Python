#Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos km você percorreu? '))
dias = int(input('Quantos dias você ficou com o carro? '))
diaria = 60 * dias
rodado = 0.15 * km
print(f'O valor total a ser pago será de R$ {diaria + rodado:.2f}')

