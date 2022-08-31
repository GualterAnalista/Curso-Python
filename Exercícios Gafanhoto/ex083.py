#Crie um programa onde o usuário digite uma expressão qualquer que
#use parênteses. Seu aplicativo deverá analisar se a expressão passada
#está com os parênteses abertos e fechados na ordem correta.

pilha = []
expr = str(input('Digite uma expressão: '))
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()#Remove o último elemento de uma lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
