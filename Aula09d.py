#TRABALHANDO COM SPLIT

frase = 'Curso em Vídeo Python'
print(frase.split())#Divide a frase formando uma lista
dividido = frase.split()
print(dividido[0])#Vai mostrar somente a palavra da posição zero, que é "Curso"
print(dividido[2][3])#Vai pegar a posição 2 (vídeo) e mostrar a letra nº3 "e"

