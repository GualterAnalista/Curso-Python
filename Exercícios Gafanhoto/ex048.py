#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
#de três e que se encontram no intervalo de 1 até 500


s = 0
cont = 0 #Este é o contador
for c in range(1,501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma de todos os {cont} valores solicitados é: {s}.')