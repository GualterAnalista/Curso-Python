#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
#como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
#Olá, Mundo!
#~~~~~~~~~

#Fazer com que a linha fique do mesmo tamanho da mensagem, mesmo que se mude a mensagem
def escreva(msg):
    tam = len(msg)
    print('~'* tam)
    print(msg)
    print('~' * tam)

escreva('Gualter Silveira')