matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite um valor para a posição {linha} {c}: '))
print('=-' * 30)
for lprint in range(0, 3):
    for cprint in range(0, 3):
        print(f'[{matriz [lprint] [cprint]:^5}]', end='')
    print()
