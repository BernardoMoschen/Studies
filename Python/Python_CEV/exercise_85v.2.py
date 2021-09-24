princ = []
impares = []
pares = []
temp = []
for i in range(0, 7):
    temp.append(int(input(f'Digite o {i+1}º valor: ')))
    if temp[i] % 2 == 0:
        pares.append(temp[i])
    else:
        impares.append(temp[i])
princ.append(impares[:])
princ.append(pares[:])
print(f'Os valores digitados foram: {princ}.')
print(f'Sendo os ímpares: {impares}.\nE os pares: {pares}')
