frase = 'Curso em Vídeo Python   '
print(frase.count('o'))#Conta quantas vezes tem a letra "o" na frase
print(frase.upper().count('O'))
print(len(frase))#Faz a contagem de caracteres dentro da frase. Inclusive os espaços
print(len(frase.strip()))#Remove espaços indesejáveis.Tem antes de Curso e final
print(frase.replace('Python', 'Android'))#Substitui uma palavra por outra
print('Curso' in frase)#Retorna True or False
print(frase.find('Curso'))#Mostra em que posição inicia a palavra "Curso"
print(frase.find('em'))#Mostra em que posição inicia a palavra "em"
print(frase.find('aula'))#Retorna -1 porque não existe esta palavra na frase
print(frase.lower().find('vídeo'))#Converte a palavra para minúscula e a acha
print(frase.split())#Divide a frase formando uma lista

