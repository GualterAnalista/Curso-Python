#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo
#de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ESCALENO: todos os lados diferentes
# – ISÓSCELES: dois lados iguais, um diferente

from colorama import Fore,Style
print(Fore.RED + '-='*15)#Para colocar cor iniciar com Fore.(escolher cor) +
print('ANALISADOR DE TRIÂNGULOS')
print('-='*15)
print(Style.RESET_ALL)#Para resetar, ou seja, voltar ao normal agora.
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if r1 == r2 == r3:
        print('Com todos os lados iguais forma-se um triângulo '+Fore.BLUE+ 'EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('Com todos os lados diferentes forma-se um triângulo '+Fore.RED+ 'ESCALENO')
    else:
        print('Com 2 lados iguais e 1 diferente forma-se um triângulo ' + Fore.GREEN + 'ISÓSCELES')
else:
    print(Fore.LIGHTRED_EX+'Os segmentos acima NÃO PODEM FORMAR um triângulo')


