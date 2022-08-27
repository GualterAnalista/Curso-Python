#Agora uma peculiaridade do PYTHON - Ainda em LISTAS

a = [2, 3, 4, 7]
b = a    #Ficando essa linha e excluindo a debaixo o nº 8 aparece nas duas listas A e B no lugar do nº 4
b = a[:] #Nessa linha cria-se uma cópia de A dentro de B. E se fizer a linha de baixo só muda no B
         #Significa pegar toda a lista A (antes e depois) e colocar na lista B
b[2] = 8 #Com esse comando vai substituir a posição 2 nas listas A e B. O nº 4 vira nº 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')