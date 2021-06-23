matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maiorValorSegunda = valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para a posição {linha} {coluna}: '))
        matriz[linha][coluna] += valor
        if valor % 2 == 0:
            pares += matriz[linha][coluna]
somaTerceiraColuna = matriz[0][2] + matriz[1][2] + matriz[2][2]
if matriz[1][2] < matriz[1][0] > matriz[1][1]:
    maiorValorSegunda = matriz[1][1]
elif matriz[1][1] > matriz[1][2]:
    maiorValorSegunda = matriz[1][1]
else:
    maiorValorSegunda = matriz[1][2]
print('=-' * 30)
print('A matriz resultante é:')
for lprint in range(0, 3):
    for cprint in range(0, 3):
        print(f'[{matriz[lprint] [cprint]:^5}]', end='')
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maiorValorSegunda}.')
