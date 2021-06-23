temp = []
principal = []
maior = menor = 0
c = 1
while True:
    temp.append(input(f'Digite o nome da {c}º pessoa: '))
    temp.append(int(input(f'Digite a idade da {c}º pessoa: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    c += 1
    resp = input('Quer continuar ? [S/N] ').upper().strip()
    while resp not in 'SsNn':
        resp = input('Tente Novamente.\nQuer continuar ? [S/N] ').upper().strip()
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg.Das correspondentes pessoas: ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg.Das correspondentes pessoas: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')
