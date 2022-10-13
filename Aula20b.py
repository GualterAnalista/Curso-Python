#CONTINUAÇÃO AULA DE FUNÇÕES COM DEF + CONTADOR
#EXPLICAÇÃO 1

def contador(* núm):  #Neste exemplo, com * será criada uma Tupla com os dados informados
    print(núm)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


#EXPLICAÇÃO 2

def contador(* núm):  #Neste exemplo será criada uma Tupla com os dados informados
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


#EXPLICAÇÃO 3
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#EXPLICAÇÃO 4 ==> Desempacotar vários valores
def soma(* valores):
    s = 0
    for num in  valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2 , 9, 4)