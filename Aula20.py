#Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
#Funções são trechos de código que podem ser executados em momentos diferentes de nossos
#códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros
#simples e múltiplos

#1ª FORMA
def mostralinha():
    print('-='*20)
mostralinha()
print(f'{"Curso em Vídeo":^40}')
mostralinha()
print(f'{"Aulas de Python":^40}')
mostralinha()
print(f'{"Aluno Gualter Silveira":^40}')
mostralinha()

print('\33[34m<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>')
#2ª FORMA
def título(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)

título(f'{"Curso em Vídeo":^40}')
título(f'{"Aulas de Python":^40}')
título(f'{"Aluno Gualter Silveira":^40}')
