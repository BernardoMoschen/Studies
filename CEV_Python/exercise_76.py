produtos = ('Lápis', 1.70,
            'Borracha', 2.0,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<15}', end='')
    else:
        print(f'R${produtos[i]:>6.2f}')
