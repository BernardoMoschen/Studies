princ = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:
        princ[1].append(valor)
print(f'Os valores digitados foram: {princ}.')
print(f'Sendo os ímpares: {princ[0]}.\nE os ímpares: {princ[1]}.')
