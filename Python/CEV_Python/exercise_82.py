num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    continuar = input('\nQuer continuar? [S/N] ').upper().strip()
    while continuar not in 'SsNn':
        continuar = (input('Tente Novamente.\nQuer continuar? [S/N] ')).upper().strip()
    if continuar in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'Os valores digitados foram: {num}.')
if len(pares) >= 1:
    print(f'Os valores pares digitados foram: {pares}.')
if len(impares) >= 1:
    print(f'Os valores ímpares digitados foram: {impares}.')
