matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maiorValorSegunda = sTerCol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz = int(input(f'Digite um valor para a posição {l} {c}: '))
print('=-' * 30)
print('A matriz resultante é:')
for lprint in range(0, 3):
    for cprint in range(0, 3):
        print(f'[{matriz[lprint] [cprint]:^5}]', end='')
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {pares}.')
for linha in range(0, 3):
    sTerCol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {sTerCol}.')
for c in range(0, 3):
    if c == 0:
        maiorValorSegunda = matriz[1][c]
    elif matriz[1][c] > maiorValorSegunda:
        maiorValorSegunda = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorValorSegunda}.')
