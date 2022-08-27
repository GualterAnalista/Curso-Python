#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.


listagem = ('Cabo V8', 20.00, 'Cabo Tipo C', 20.00, 'Carregador V8', 38.00, 'Fone de Ouvido', 22.00, 'Roteador 4 antenas', 290.00,
            'Caixa de som Bluetooth', 65.00, 'Suporte Magnético', 25.00, 'Pilha AA Recarregável', 28.00, 'Pen drive 8GB', 40.00,
            'Pen drive 16GB', 50.00, 'Cartão de Memória 32GB', 50.00, 'Cabo OTG V8', 12.00)
print('='*49)
print(f'{"LISTA DE PREÇOS":^48}')
print('='*49)
for pos in range(0, len(listagem)): #Essa pos significa a posição do produto, que estará sempre em PAR.
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*49)